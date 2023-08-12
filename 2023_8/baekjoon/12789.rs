use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let buf = buf.split_ascii_whitespace().flat_map(str::parse::<i32>);
    let begin: Vec<i32> = buf.skip(1).collect();
    let mut stack: Vec<i32> = Vec::new();
    let mut target = 1;

    for i in 0..begin.len() {
        if begin[i] == target {
            target += 1;
        } else {
            stack.push(begin[i])
        }
        while let Some(top) = stack.last() {
            if *top != target {
                break;
            }
            stack.pop();
            target += 1;
        }
    }
    println!("{}", if stack.len() != 0 { "Sad" } else { "Nice" });
}
