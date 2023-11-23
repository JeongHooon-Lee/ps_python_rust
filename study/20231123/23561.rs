#![no_main]
use std::io::{stdin, Read};

#[no_mangle]
unsafe fn main() -> i32 {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut buf = buf.split_ascii_whitespace().map(|x| x.parse()).flatten();
    let n: usize = buf.next().unwrap();
    let mut arr: Vec<_> = buf.collect();
    arr.sort_unstable();
    let result = arr[2 * n - 1] - arr[n];
    write(1, result.to_string().as_ptr(), result.to_string().len());
    0
}
#[link(name = "c")]
extern "C" {
    fn write(fd: u32, s: *const u8, len: usize);
}
