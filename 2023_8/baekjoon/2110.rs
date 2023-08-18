use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut buf = buf.split_ascii_whitespace();
    let mut iterator = || buf.next().unwrap().parse::<usize>().unwrap();
    let (n, c) = (iterator(), iterator());
    let mut routers: Vec<usize> = Vec::new();
    for _ in 0..n {
        routers.push(iterator());
    }
    routers.sort();
    println!(
        "{}",
        solution(1, routers.last().unwrap() - routers[0], &routers, c)
    );
}

fn solution(mut start: usize, mut end: usize, routers: &Vec<usize>, target: usize) -> usize {
    let mut result = 0;
    while start <= end {
        let mid = ((start + end) / 2) as usize;
        let mut count = 1;
        let mut last_pos = routers[0];

        for next in routers.iter().skip(1) {
            if next - last_pos >= mid {
                count += 1;
                last_pos = *next;
            }
        }

        if count >= target {
            start = mid + 1;
            result = mid;
        } else {
            end = mid - 1;
        }
    }
    result
}
