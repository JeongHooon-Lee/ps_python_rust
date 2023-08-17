use std::io::{stdin, BufRead, Read};

struct Info {
    n: usize,
    m: usize,
    k: usize,
}

fn main() {
    let mut buf = String::new();
    stdin().lock().read_line(&mut buf).unwrap();
    let infos: Info = {
        let parts: Vec<usize> = buf
            .split_ascii_whitespace()
            .map(|s| s.parse::<usize>().unwrap())
            .collect();
        Info {
            n: parts[0],
            m: parts[1],
            k: parts[2],
        }
    };
    buf.clear();
    stdin().read_to_string(&mut buf).unwrap();
    let arr: Vec<Vec<char>> = buf
        .lines()
        .skip(0)
        .map(|line| line.chars().collect())
        .collect();

    println!(
        "{}",
        solution(&infos, 'W', &arr).min(solution(&infos, 'B', &arr))
    );
}

fn solution(info: &Info, color: char, arr: &Vec<Vec<char>>) -> usize {
    let mut dp = vec![vec![0; info.m + 1]; info.n + 1];
    let mut result = info.n * info.m;

    for i in 0..info.n {
        for j in 0..info.m {
            let value;
            if (i + j) % 2 == 0 {
                value = (color != arr[i][j]) as usize;
            } else {
                value = (color == arr[i][j]) as usize;
            }

            dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1] - dp[i][j] + value;
        }
    }

    for i in 1..(info.n - info.k + 2) {
        for j in 1..(info.m - info.k + 2) {
            result = result.min(
                dp[i + info.k - 1][j + info.k - 1]
                    - dp[i - 1][j + info.k - 1]
                    - dp[i + info.k - 1][j - 1]
                    + dp[i - 1][j - 1],
            )
        }
    }
    result
}
