use aisi_trivector_basic::{retention, utilization};
fn main() {
    println!("rho: {:?}", utilization(Some(25), Some(100)));
    println!("(L,Q): {:?}", retention(&[true, false]));
}
