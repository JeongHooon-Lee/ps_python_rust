#![no_main]
use std::io::{stdin, Read};

#[no_mangle]
unsafe fn main() -> i32 {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut inputs = buf
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>())
        .flatten();
    let _N = inputs.next().unwrap();
    let arr: Vec<usize> = inputs.collect();
    let mut dp = vec![0; 1_000_001];
    let mut result = 0;

    for v in arr {
        dp[v] = dp[v].max(dp[v - 1] + 1);
        result = result.max(dp[v]);
    }
    write(1, result.to_string().as_ptr(), result.to_string().len());
    0
}

#[link(name = "c")]
extern "C" {
    fn write(fd: u32, s: *const u8, len: usize);
}
