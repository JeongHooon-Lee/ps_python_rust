use std::collections::VecDeque;
use std::io::stdin;

fn main() {
    for _ in 0..get_line().trim().parse::<usize>().unwrap() {
        let (M, N, map, p_position) = get_info();

        let mut queue: VecDeque<(Position, Position, String)> = VecDeque::new();
        let mut visited = vec![vec![vec![vec![false; N]; M]; N]; M];

        visited[p_position[0].0][p_position[0].1][p_position[1].0][p_position[1].1] = true;
        queue.push_back((p_position[0], p_position[1], String::new()));
        let mut result = String::new();

        while let Some((p1, p2, history)) = queue.pop_front() {
            if p1 == p2 {
                result = history;
                break;
            }

            for (x_diff, y_diff, c) in [(-1, 0, 'N'), (0, -1, 'W'), (1, 0, 'S'), (0, 1, 'E')] {
                let next_p1 = next_pos(p1, x_diff, y_diff, M, N, &map);
                let next_p2 = next_pos(p2, x_diff, y_diff, M, N, &map);

                if map[next_p1.0][next_p1.1] != 3 && map[next_p2.0][next_p2.1] != 3 {
                    if (next_p1 == p1 && next_p2 == p2)
                        || visited[next_p1.0][next_p1.1][next_p2.0][next_p2.1]
                    {
                        continue;
                    }

                    visited[next_p1.0][next_p1.1][next_p2.0][next_p2.1] = true;
                    let mut next_result = history.clone();
                    next_result.push(c);
                    queue.push_back((next_p1, next_p2, next_result));
                }
            }
        }

        match result.is_empty() {
            true => println!("IMPOSSIBLE"),
            false => println!("{} {}", result.len(), result),
        }
    }
}

fn next_pos(
    current: Position,
    x_diff: i32,
    y_diff: i32,
    m: usize,
    n: usize,
    map: &Vec<Vec<usize>>,
) -> Position {
    let mut next_x = current.0 as i32 + x_diff;
    let mut next_y = current.1 as i32 + y_diff;

    if next_x < 0 {
        next_x = (m - 1) as i32;
    } else if next_x == m as i32 {
        next_x = 0;
    }

    if next_y < 0 {
        next_y = (n - 1) as i32;
    } else if next_y == n as i32 {
        next_y = 0;
    }

    match map[next_x as usize][next_y as usize] == 2 {
        true => current,
        false => Position(next_x as usize, next_y as usize),
    }
}

fn get_info() -> (usize, usize, Vec<Vec<usize>>, Vec<Position>) {
    let line = get_line();
    let mut iter = line
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>().unwrap());
    let (M, N): (usize, usize) = (iter.next().unwrap(), iter.next().unwrap());
    let (map, p_position) = get_map(M, N);

    (M, N, map, p_position)
}

fn get_line() -> String {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();
    buf
}

#[derive(Clone, Copy, PartialEq)]
struct Position(usize, usize);

fn get_map(M: usize, N: usize) -> (Vec<Vec<usize>>, Vec<Position>) {
    let mut map = vec![vec![0; N]; M];
    let mut p_position = Vec::new();
    for i in 0..M {
        let line = get_line();
        for (inx, c) in line.char_indices() {
            map[i][inx] = match c {
                'P' => {
                    p_position.push(Position(i, inx));
                    1
                }
                'X' => 2,
                'G' => 3,
                _ => continue,
            };
        }
    }
    (map, p_position)
}
