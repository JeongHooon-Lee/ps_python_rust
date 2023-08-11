use std::io::stdin;

fn main() {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();
    let mut buf = buf.split_whitespace();

    let n = buf.next().unwrap().parse::<u32>().unwrap();
    let k = buf.next().unwrap().parse::<usize>().unwrap();
    let mut divisor: Vec<u32> = vec![1, n];

    for i in 2..((n as f32).sqrt() as u32 + 1) {
        if n % i == 0 {
            divisor.push(i);
            if n / i != i {
                divisor.push(n / i);
            }
        }
    }

    if divisor.len() < k {
        println!("0");
    } else {
        divisor.sort();
        println!("{}", divisor[k - 1]);
    }
    return;
}
