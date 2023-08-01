use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).expect("Failed to read");
    let mut iterator = buf.split_whitespace().flat_map(str::parse::<i32>);
    let mut iterator = || iterator.next().unwrap();

    let a = iterator();
    let b = iterator();

    println!("{}", (a + b) * (a - b));
    return;
}
