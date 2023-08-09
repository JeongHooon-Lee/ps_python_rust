use std::io::stdin;

fn main() {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();
    let s: Vec<char> = buf.trim().chars().collect();

    let n = s.len();
    for i in 0..(n / 2) {
        if s[i] != s[n - i - 1] {
            println!("0");
            return;
        }
    }
    println!("1");
    return;
}
