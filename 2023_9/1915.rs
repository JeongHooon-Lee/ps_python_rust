use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut arr: Vec<Vec<u32>> = buf
        .lines()
        .skip(1)
        .map(|line| line.chars().map(|c| c.to_digit(10).unwrap()).collect())
        .collect();
    let n = arr.len();
    let m = arr[0].len();
    let mut result = 0;

    for i in 0..n {
        for j in 0..m {
            if i >= 1
                && j >= 1
                && arr[i][j] == 1
                && arr[i][j - 1] != 0
                && arr[i - 1][j] != 0
                && arr[i - 1][j - 1] != 0
            {
                arr[i][j] = arr[i][j - 1].min(arr[i - 1][j].min(arr[i - 1][j - 1])) + 1;
            }
            result = result.max(arr[i][j].pow(2));
        }
    }
    println!("{}", result);
}
