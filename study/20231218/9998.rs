use std::io::stdin;

fn main() {
    let (n, yk, dk) = get_inputs();
    let mut left = (n - 1) / 2;
    let mut right: usize = 1_000_000_000_000;
    let mut answer = usize::MAX;

    while left < right {
        let mid_1 = left + (right - left) / 3;
        let mid_2 = left + ((right - left) / 3) * 2;
        let v_1 = calculate(&yk, mid_1, n) + calculate(&dk, mid_1, n);
        let v_2 = calculate(&yk, mid_2, n) + calculate(&dk, mid_2, n);

        answer = answer.min(v_1).min(v_2);

        if left == mid_1 {
            break;
        }
        if v_1 > v_2 {
            left = mid_1;
        } else {
            right = mid_2;
        }
    }

    println!("{}", answer);
}

fn calculate(yk: &[usize], mut value: usize, n: usize) -> usize {
    let mut result = 0;
    value += 1;
    for i in 0..n {
        match i <= n / 2 {
            true => value -= 1,
            false => value += 1,
        }
        result += match yk[i] >= value {
            true => yk[i] - value,
            false => value - yk[i],
        };
    }

    result
}

fn get_line() -> String {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();
    buf
}

fn get_inputs() -> (usize, Vec<usize>, Vec<usize>) {
    let n = get_line().trim().parse::<usize>().unwrap();
    let yk: Vec<usize> = get_line()
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>().unwrap())
        .collect();
    let dk: Vec<usize> = get_line()
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>().unwrap())
        .collect();

    (n, yk, dk)
}
