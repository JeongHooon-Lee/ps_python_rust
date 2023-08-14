use std::collections::VecDeque;
use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().lock().read_to_string(&mut buf).unwrap();
    let lines: Vec<Vec<i32>> = buf
        .lines()
        .map(|line| {
            line.split_ascii_whitespace()
                .map(|x| x.parse::<i32>().unwrap())
                .collect()
        })
        .collect();

    let status: &Vec<_> = &lines[1];
    let mut values: VecDeque<_> = lines[2]
        .iter()
        .enumerate()
        .filter(|(inx, _)| status[*inx] == 0)
        .map(|(_, v)| v)
        .collect();

    for v in lines[4].iter() {
        values.push_front(v);
        print!("{} ", values.pop_back().unwrap());
    }
}
