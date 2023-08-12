use std::io::{stdin, BufRead};

fn main() {
    let mut buf = String::new();
    stdin().lock().read_line(&mut buf).unwrap();
    let buf = buf.trim().parse::<f64>().unwrap();

    println!("{}", (buf.sqrt() as u32));
}
