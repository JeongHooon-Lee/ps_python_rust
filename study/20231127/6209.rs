use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut buf_iter = buf
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>())
        .flatten();
    let mut iterator = || buf_iter.next().unwrap();
    let (d, n, m) = (iterator(), iterator(), iterator());
    let mut stones: Vec<usize> = buf_iter.collect();
    stones.extend(Vec::from([0, d]));
    stones.sort_unstable();

    let mut result = 0;
    let mut left = 0;
    let mut right = d;

    while left <= right {
        let mid = (left + right) >> 1;
        let mut counter = 0;
        let mut pos = 0;

        for i in 1..(n + 2) {
            match stones[i] - stones[pos] < mid {
                true => counter += 1,
                false => pos = i,
            }
        }

        match counter > m {
            true => right = mid - 1,
            false => {
                result = mid;
                left = mid + 1;
            }
        }
    }
    println!("{:?}", result);
}

// 0 2 11 14 17 22 25
// 2 9 3 3 5 3
