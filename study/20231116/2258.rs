use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let first_line = buf.lines().next().unwrap();
    let mut iterator = first_line
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>())
        .flatten();
    let (n, m) = (iterator.next().unwrap(), iterator.next().unwrap());

    let mut infos: Vec<(usize, usize)> = buf
        .lines()
        .skip(1)
        .map(|line| {
            let numbers: Vec<usize> = line
                .split_ascii_whitespace()
                .map(|x| x.parse::<usize>().unwrap())
                .collect();
            (numbers[0], numbers[1])
        })
        .collect();
    infos.sort_by(|a, b| {
        if a.1 != b.1 {
            a.1.cmp(&b.1)
        } else {
            b.0.cmp(&a.0)
        }
    });

    let mut current_weight = 0;
    let mut current_price = 0;
    let mut result = i32::MAX;

    for i in 0..n {
        current_weight += infos[i].0;
        if i >= 1 && infos[i].1 == infos[i - 1].1 {
            current_price += infos[i].1;
        } else {
            current_price = infos[i].1;
        }

        if current_weight >= m {
            result = result.min(current_price as i32);
        }
    }
    if current_weight < m {
        println!("-1");
    } else {
        println!("{}", result);
    }
}
