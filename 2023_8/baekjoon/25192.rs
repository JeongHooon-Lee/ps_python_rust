#![no_main]
use std::collections::HashSet;
use std::io::{stdin, Read};
// use std::iter::FromIterator;

#[no_mangle]
unsafe fn main() -> i32 {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();

    let buf: Vec<_> = buf.lines().skip(2).collect();
    let ans: usize = buf
        .split(|&v| v == "ENTER")
        .map(|names| HashSet::<_>::from_iter(names).len())
        .sum();
    write(1, ans.to_string().as_ptr(), ans.to_string().len());
    0
}

#[link(name = "c")]
extern "C" {
    fn write(fd: u32, s: *const u8, len: usize);
}
