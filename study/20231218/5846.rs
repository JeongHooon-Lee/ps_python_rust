use std::collections::VecDeque;
use std::io::{stdin, Read};

fn main() {
    let (n, field) = get_inputs();

    let mut left = 0;
    let mut right = *field.iter().flat_map(|row| row.iter()).max().unwrap() as usize;
    let mut answer = right;
    let target = match n % 2 {
        0 => (n * n) / 2,
        1 => (n * n) / 2 + 1,
        _ => unreachable!(),
    };

    while left <= right {
        let mid = (left + right) / 2;
        let mut result = 0;
        let mut is_visited = vec![vec![false; n]; n];

        for i in 0..n {
            for j in 0..n {
                if !is_visited[i][j] {
                    is_visited[i][j] = true;
                    result = result.max(bfs(&field, &mut is_visited, n, mid, (i, j)));
                }
            }
        }

        if result >= target {
            answer = answer.min(mid);
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    println!("{}", answer);
}

fn bfs(
    field: &Vec<Vec<isize>>,
    is_visited: &mut Vec<Vec<bool>>,
    n: usize,
    values: usize,
    (x, y): (usize, usize),
) -> usize {
    let mut queue = VecDeque::new();
    let mut counter = 1;
    queue.push_back((x, y));

    while let Some(v) = queue.pop_front() {
        for (diff_x, diff_y) in [(-1, 0), (0, -1), (1, 0), (0, 1)] {
            let next_x = v.0 as isize + diff_x;
            let next_y = v.1 as isize + diff_y;

            if next_x >= 0 && next_x < n as isize && next_y >= 0 && next_y < n as isize {
                let next_x = next_x as usize;
                let next_y = next_y as usize;
                let diff = field[v.0][v.1] - field[next_x][next_y];
                if !is_visited[next_x][next_y] && diff.abs() <= values as isize {
                    counter += 1;
                    is_visited[next_x][next_y] = true;
                    queue.push_back((next_x as usize, next_y as usize));
                }
            }
        }
    }
    counter
}

fn get_inputs() -> (usize, Vec<Vec<isize>>) {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut field: Vec<Vec<isize>> = buf
        .lines()
        .skip(1)
        .map(|line| {
            line.split_ascii_whitespace()
                .map(|x| x.parse::<isize>().unwrap())
                .collect()
        })
        .collect();

    (field[0].len(), field)
}
