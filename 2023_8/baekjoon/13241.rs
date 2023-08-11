use std::io::stdin;

fn main() {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();
    let mut buf = buf.split_whitespace().map(|x| x.parse().unwrap());
    let (a, b): (usize, usize) = (buf.next().unwrap(), buf.next().unwrap());
    let (mut c, mut d) = (a.max(b), a.min(b));

    while c % d != 0 {
        (c, d) = (d, c % d);
    }
    println!("{}", a * b / d);
}
