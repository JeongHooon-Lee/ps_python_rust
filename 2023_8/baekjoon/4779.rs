use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let buf: Vec<_> = buf
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>().unwrap())
        .collect();

    for v in buf {
        let mut line = vec!['-'; 3_usize.pow(v as u32)];
        let len = line.len();
        println!(
            "{}",
            recursion(&mut line, 0, len).iter().collect::<String>()
        );
    }
}

fn recursion(line: &mut Vec<char>, start: usize, end: usize) -> Vec<char> {
    if start + 1 == end {
        return vec!['-'];
    }
    let steps = (end - start) / 3;
    let mut result1 = recursion(line, start, start + steps);
    let result2 = recursion(line, start + steps * 2, end);
    result1.extend(vec![' '; steps]);
    result1.extend(result2);
    result1
}
