use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut buf = buf.split_ascii_whitespace();
    let mut iterator = || buf.next().unwrap().parse::<usize>().unwrap();

    let (a, b, c, d) = (iterator(), iterator(), iterator(), iterator());
    let (e, f) = (a * d + b * c, b * d);
    let (mut g, mut h) = (e, f);
    while g % h != 0 {
        (g, h) = (h, g % h);
    }
    println!("{} {}", e / h, f / h);
}
