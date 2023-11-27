use std::collections::VecDeque;
use std::io::{self, Read};

fn main() {
    let (r, c, matrix, moves): (i32, i32, Vec<Vec<i32>>, Vec<(i32, i32)>) = inputs();

    println!("{}", solve(r, c, matrix, moves));
}

fn solve(r: i32, c: i32, matrix: Vec<Vec<i32>>, moves: Vec<(i32, i32)>) -> i32 {
    let mut visited: Vec<Vec<bool>> = vec![vec![false; c as usize]; r as usize];
    let mut queue: VecDeque<(i32, i32, i32)> = matrix[0]
        .iter()
        .enumerate()
        .filter(|(_, &values)| values == 1)
        .map(|(inx, _)| {
            visited[0][inx] = true;
            (0, 0, inx as i32)
        })
        .collect();

    while let Some((v, new_r, new_c)) = queue.pop_front() {
        if new_r == r - 1 {
            return v;
        }
        for (diff_r, diff_c) in moves.iter() {
            let (next_r, next_c) = (new_r + diff_r, new_c + diff_c);

            if next_r < 0
                || next_c < 0
                || next_r >= r
                || next_c >= c
                || matrix[next_r as usize][next_c as usize] == 0
                || visited[next_r as usize][next_c as usize]
            {
                continue;
            }
            visited[next_r as usize][next_c as usize] = true;
            queue.push_back((v + 1, next_r, next_c));
        }
    }
    -1
}

fn inputs() -> (i32, i32, Vec<Vec<i32>>, Vec<(i32, i32)>) {
    // 입력 받기
    let mut buf = String::new();
    io::stdin().read_to_string(&mut buf).unwrap();

    // 첫 행 파싱
    let mut iter = buf.lines();
    let (r, c): (i32, i32) = {
        let mut iter = iter.next().unwrap().split_whitespace();
        let r: i32 = iter.next().unwrap().parse().unwrap();
        let c: i32 = iter.next().unwrap().parse().unwrap();
        (r, c)
    };

    // 행렬 파싱
    let matrix: Vec<Vec<i32>> = iter
        .take(r as usize)
        .map(|line| {
            line.split_whitespace()
                .map(|x| x.parse().unwrap())
                .collect()
        })
        .collect();

    // 좌표 파싱
    let moves: Vec<(i32, i32)> = buf
        .lines()
        .skip(r as usize + 2)
        .map(|line| {
            let mut iter = line.split_whitespace();
            let x: i32 = iter.next().unwrap().parse().unwrap();
            let y: i32 = iter.next().unwrap().parse().unwrap();
            (x, y)
        })
        .collect();

    (r, c, matrix, moves)
}
