use std::collections::VecDeque;
use std::fmt::Write;
use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().lock().read_to_string(&mut buf).unwrap();
    let mut buf = buf.split_ascii_whitespace();
    let mut iterator = || buf.next().unwrap().parse::<i32>().unwrap();
    let mut output = String::new();

    let mut deque: VecDeque<i32> = VecDeque::new();
    for _ in 0..iterator() {
        match iterator() {
            1 => deque.push_front(iterator()),
            2 => deque.push_back(iterator()),
            3 => writeln!(output, "{}", deque.pop_front().unwrap_or(-1)).unwrap(),
            4 => writeln!(output, "{}", deque.pop_back().unwrap_or(-1)).unwrap(),
            5 => writeln!(output, "{}", deque.len()).unwrap(),
            6 => writeln!(output, "{}", deque.is_empty() as i8).unwrap(),
            7 => writeln!(output, "{}", deque.front().unwrap_or(&-1)).unwrap(),
            8 => writeln!(output, "{}", deque.back().unwrap_or(&-1)).unwrap(),
            _ => unreachable!(),
        }
    }
    println!("{}", output);
}
