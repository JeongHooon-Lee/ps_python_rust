use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut buf = buf.split_ascii_whitespace();
    let mut iterator = || buf.next().unwrap().parse::<usize>().unwrap();
    let primes = get_primes();

    for _ in 0..iterator() {
        let mut result = 0;
        let n = iterator();
        for prime in 1..(1_000_000 + 1) {
            if !primes[prime] {
                continue;
            }
            if prime > (n / 2) {
                break;
            }
            if primes[n - prime] {
                result += 1;
            }
        }
        println!("{}", result);
    }
}

fn get_primes() -> Vec<bool> {
    let limit = 1000000;
    let mut nums = vec![true; limit + 1];
    nums[1] = false;

    let mut i = 2;
    while i * i <= limit {
        if nums[i] {
            for j in ((i * i)..(limit + 1)).step_by(i) {
                nums[j] = false;
            }
        }
        i += 1;
    }

    nums
}
