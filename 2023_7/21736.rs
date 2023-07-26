use std::collections::VecDeque;
use std::io::{stdin, Read};

struct Pos {
    x: i32,
    y: i32,
}
struct MapSize {
    n: usize,
    m: usize,
}

fn main() {
    let mut buf: String = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut arr: Vec<Vec<char>> = Vec::new();
    let mut start_pos = Pos { x: 600, y: 600 };
    let mut x = 0;
    for line in buf.lines().skip(1) {
        let char_vector: Vec<char> = line.trim().chars().collect();
        if let Some(index) = char_vector.iter().position(|&v| v == 'I') {
            start_pos.x = x as i32;
            start_pos.y = index as i32;
        }
        x += 1;
        arr.push(char_vector)
    }
    let map: MapSize = MapSize {
        n: arr.len(),
        m: arr[0].len(),
    };

    let res = bfs(start_pos, map, arr);
    if res == 0 {
        println!("TT");
    } else {
        println!("{}", res);
    }
}

fn is_valid(x: i32, y: i32, map: &MapSize) -> bool {
    return 0 <= x && (x as usize) < map.n && 0 <= y && (y as usize) < map.m;
}

fn bfs(start_pos: Pos, map: MapSize, field: Vec<Vec<char>>) -> usize {
    let mut queue: VecDeque<Pos> = VecDeque::new();
    let mut visited: Vec<Vec<i32>> = vec![vec![0; map.m]; map.n];
    let way: [(i32, i32); 4] = [(-1, 0), (1, 0), (0, 1), (0, -1)];
    visited[start_pos.x as usize][start_pos.y as usize] = 1;
    queue.push_back(start_pos);
    let mut result = 0;

    while let Some(info) = queue.pop_front() {
        for i in way.iter() {
            let next_x: i32 = info.x + i.0;
            let next_y: i32 = info.y + i.1;
            if is_valid(next_x, next_y, &map)
                && visited[next_x as usize][next_y as usize] != 1
                && field[next_x as usize][next_y as usize] != 'X'
            {
                visited[next_x as usize][next_y as usize] = 1;
                if field[next_x as usize][next_y as usize] == 'P' {
                    result += 1;
                }
                queue.push_back(Pos {
                    x: next_x,
                    y: next_y,
                });
            }
        }
    }
    result
}
