use std::io::stdin;

fn std_input() -> i32 {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();
    let buf = buf.trim().parse::<i32>().unwrap();
    buf
}

fn main() {
    let t = std_input();
    let money = [25, 10, 5, 1];

    for _ in 0..t {
        let mut buf = std_input();
        // let mut answer = 0;
        for m in money {
            print!("{} ", buf / m);
            buf %= m;
        }
        println!();
    }
    return;
}
