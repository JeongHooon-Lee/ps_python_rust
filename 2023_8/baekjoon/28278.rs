use std::fmt::Write;
use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut buf = buf.split_ascii_whitespace();
    let mut iterator = || buf.next().unwrap().parse().unwrap();
    let mut stack: Vec<i32> = Vec::with_capacity(1_000_000);
    let mut output = String::new();

    for _ in 0..iterator() {
        // let n = iterator();
        match iterator() {
            1 => {
                stack.push(iterator());
                continue;
            }
            2 => writeln!(output, "{}", stack.pop().unwrap_or(-1)),
            3 => writeln!(output, "{}", stack.len()),
            4 => writeln!(output, "{}", stack.is_empty() as u8),
            5 => writeln!(output, "{}", stack.last().unwrap_or(&-1)),
            _ => unreachable!(),
        }
        .unwrap();
    }
    print!("{output}");
}
