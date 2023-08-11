use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut buf = buf.split_ascii_whitespace();
    let mut iterator = || buf.next().unwrap().parse::<usize>().unwrap();

    let n = iterator();
    let mut nums: Vec<usize> = Vec::new();
    let mut spaces: Vec<usize> = Vec::new();
    let mut last_num = 0;
    for i in 1..=n {
        let num = iterator();
        spaces.push(num - last_num);
        last_num = num;
        if i == 1 || i == n {
            nums.push(num);
        }
    }

    let mut gcd = spaces[1];
    for space in spaces.iter().skip(2) {
        gcd = get_gcd(gcd, *space);
    }

    println!("{}", (nums[1] - nums[0]) / gcd + 1 - n);
}

fn get_gcd(a: usize, b: usize) -> usize {
    let (mut c, mut d) = (a.max(b), a.min(b));

    while c % d != 0 {
        (c, d) = (d, c % d);
    }
    return d;
}
