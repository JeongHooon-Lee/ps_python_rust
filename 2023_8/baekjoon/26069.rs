#![no_main]
use std::collections::HashSet;
use std::io::{stdin, Read};

#[no_mangle]
unsafe fn main() -> i32 {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let buf: Vec<&str> = buf.lines().collect();
    let n = buf[0].parse::<i32>().unwrap();
    let mut dancing: HashSet<&str> = HashSet::with_capacity(1000);
    dancing.insert("ChongChong");
    for i in 1..=n {
        let people: Vec<_> = buf[i as usize].split_ascii_whitespace().collect();
        dancing
            .contains(people[0])
            .then(|| dancing.insert(people[1]));
        dancing
            .contains(people[1])
            .then(|| dancing.insert(people[0]));
    }
    write(
        1,
        dancing.len().to_string().as_ptr(),
        dancing.len().to_string().len(),
    );
    0
    // println!("{}", dancing.len());
}

#[link(name = "c")]
extern "C" {
    fn write(fd: u32, s: *const u8, len: usize);
}
