// SPDX-License-Identifier: LGPL-2.1-only
//! Proposed continuity arithmetic. Not a model, reasoner, or physical theory.
#[derive(Debug, PartialEq)]
pub enum MetricError { InvalidInput }

pub fn utilization(tokens: Option<u64>, capacity: Option<u64>) -> Result<Option<f64>, MetricError> {
    match (tokens, capacity) {
        (Some(n), Some(c)) if c > 0 && n <= c => Ok(Some(n as f64 / c as f64)),
        (Some(_), Some(_)) => Err(MetricError::InvalidInput),
        _ => Ok(None),
    }
}

pub fn retention(outcomes: &[bool]) -> Option<(f64, f64)> {
    if outcomes.is_empty() { return None; }
    let loss = outcomes.iter().filter(|&&x| !x).count() as f64 / outcomes.len() as f64;
    Some((loss, 1.0 - loss))
}

pub fn objective(d: Option<f64>, loss: Option<f64>, cost: Option<f64>, lambda: Option<f64>, mu: Option<f64>) -> Result<Option<f64>, MetricError> {
    match (d, loss, cost, lambda, mu) {
        (Some(d), Some(l), Some(c), Some(a), Some(b)) => {
            if [d,l,c,a,b].iter().any(|x| !x.is_finite() || *x < 0.0) || l > 1.0 {
                return Err(MetricError::InvalidInput);
            }
            let value = d + a*l + b*c;
            if !value.is_finite() { return Err(MetricError::InvalidInput); }
            Ok(Some(value))
        },
        _ => Ok(None),
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test] fn ratio() { assert_eq!(utilization(Some(25),Some(100)),Ok(Some(0.25))); }
    #[test] fn unknown() { assert_eq!(utilization(None,Some(100)),Ok(None)); }
    #[test] fn zero_capacity() { assert_eq!(utilization(Some(0),Some(0)),Err(MetricError::InvalidInput)); }
    #[test] fn over_capacity() { assert!(utilization(Some(101),Some(100)).is_err()); }
    #[test] fn empty() { assert_eq!(retention(&[]),None); }
    #[test] fn partial() { assert_eq!(retention(&[true,false]),Some((0.5,0.5))); }
    #[test] fn perfect() { assert_eq!(retention(&[true,true]),Some((0.0,1.0))); }
    #[test] fn obj() { assert!((objective(Some(0.2),Some(0.5),Some(2.0),Some(1.0),Some(0.1)).unwrap().unwrap()-0.9).abs()<1e-12); }
    #[test] fn obj_unknown() { assert_eq!(objective(None,Some(0.0),Some(1.0),Some(1.0),Some(1.0)),Ok(None)); }
    #[test] fn obj_nan() { assert!(objective(Some(f64::NAN),Some(0.0),Some(1.0),Some(1.0),Some(1.0)).is_err()); }
    #[test] fn obj_bad_loss() { assert!(objective(Some(0.0),Some(2.0),Some(1.0),Some(1.0),Some(1.0)).is_err()); }
}
