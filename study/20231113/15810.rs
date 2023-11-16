use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut inputs = buf
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>())
        .flatten();
    let mut iterator = || inputs.next().unwrap();
    let (_N, M) = (iterator(), iterator());
    let staff: Vec<usize> = inputs.collect();

    let mut right = *staff.iter().min().unwrap() * M;
    let mut left = 1;
    let mut answer = M;

    while left <= right {
        let mid = (left + right) / 2 as usize;
        let result = solution(&staff, mid);

        if result >= M {
            answer = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    println!("{}", answer);
}

fn solution(staff: &Vec<usize>, times: usize) -> usize {
    staff.iter().map(|x| times / x).sum()
}
