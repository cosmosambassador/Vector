# Rust crate

Source-only starter. Run `cargo test` and `cargo run --example basic`.
`Option` represents unknown or undefined results; `Result` reports invalid input.
Tokens and capacity use u64. Ratios use f64 and are approximate for very large counts.
The Python API accepts finite numeric values, while Rust token counts are integers.
A future API alignment review must decide whether Python should enforce integer counts.
No pkgsrc-rs dependency is enabled: package inspection is a distinct feature from text reasoning.
License: LGPL-2.1-only; full text is in ../LICENSE.
