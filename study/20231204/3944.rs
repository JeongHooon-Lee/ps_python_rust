use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut buf_iter = buf.split_ascii_whitespace();
    let mut iterator = || buf_iter.next().unwrap();

    for _ in 0..iterator().parse::<usize>().unwrap() {
        let (b, d) = (iterator().parse::<usize>().unwrap(), iterator().chars());
        let mut values = 0;
        d.for_each(|c| values += c.to_digit(10).unwrap());
        println!("{}", values as usize % (b - 1));
    }
}
