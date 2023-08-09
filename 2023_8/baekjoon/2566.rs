use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let arr: Vec<Vec<u32>> = buf
        .lines()
        .map(|line| {
            line.split_ascii_whitespace()
                .map(|n| n.parse::<u32>().unwrap())
                .collect()
        })
        .collect();

    let mut max_value = arr[0][0];
    let mut max_index = (1, 1);
    for (i, row) in arr.iter().enumerate() {
        for (j, &num) in row.iter().enumerate() {
            if num > max_value {
                max_value = num;
                max_index = (i + 1, j + 1);
            }
        }
    }

    println!("{}", max_value);
    println!("{} {}", max_index.0, max_index.1);
}
