use std::io::stdin;

fn main() {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();
    let buf = buf.trim().parse().unwrap();

    let mut answer = 2;
    for _ in 0..buf {
        answer = answer * 2 - 1;
    }
    println!("{}", answer * answer);
}
