use std::collections::VecDeque;
use std::io::{stdin, Read};

#[derive(Debug, PartialEq)]
struct Pos {
    r: i32,
    c: i32,
}

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut inputs = buf
        .split_ascii_whitespace()
        .map(|x| x.parse::<i32>())
        .flatten();
    let mut iterator = || inputs.next().unwrap();

    let start_pos = Pos {
        r: iterator(),
        c: iterator(),
    };
    let end_pos = Pos {
        r: iterator(),
        c: iterator(),
    };

    println!("{}", solution(start_pos, end_pos));
}

fn solution(start_pos: Pos, end_pos: Pos) -> i16 {
    struct Element {
        pos: Pos,
        moved: i16,
    }
    let arr1 = vec![(3, 2), (2, 3)];
    let arr2 = vec![(-1, 1), (-1, -1), (1, 1), (1, -1)];
    let arr3: Vec<(i32, i32)> = arr1
        .iter()
        .flat_map(|&(a, b)| arr2.iter().map(move |&(c, d)| (a * c, b * d)))
        .collect();
    let mut queue: VecDeque<Element> = VecDeque::new();
    queue.push_back(Element {
        pos: start_pos,
        moved: 0,
    });

    while let Some(e) = queue.pop_front() {
        if e.pos == end_pos {
            return e.moved;
        }
        for (r_diff, c_diff) in arr3.iter() {
            if is_blocked(&e.pos, *r_diff, *c_diff, &end_pos) {
                continue;
            }
            let new_r = e.pos.r + r_diff;
            let new_c = e.pos.c + c_diff;
            if out_of_range(new_r, new_c) {
                continue;
            };

            let new_pos = Pos { r: new_r, c: new_c };
            if new_pos == end_pos {
                return e.moved + 1;
            } else {
                queue.push_back(Element {
                    pos: new_pos,
                    moved: e.moved + 1,
                })
            }
        }
    }
    -1
}

fn is_blocked(current_pos: &Pos, mut r_diff: i32, mut c_diff: i32, end_pos: &Pos) -> bool {
    let mut new_pos = Pos {
        r: current_pos.r,
        c: current_pos.c,
    };

    if r_diff == 3 || r_diff == -3 {
        new_pos.r += r_diff / 3;
        r_diff -= r_diff / 3;
    } else {
        new_pos.c += c_diff / 3;
        c_diff -= c_diff / 3;
    }

    if new_pos == *end_pos {
        return true;
    }
    new_pos.r += r_diff / 2;
    new_pos.c += c_diff / 2;
    if new_pos == *end_pos {
        return true;
    }
    false
}
fn out_of_range(r: i32, c: i32) -> bool {
    if 0 > r || r > 9 {
        return true;
    } else if 0 > c || c > 8 {
        return true;
    } else {
        return false;
    }
}
