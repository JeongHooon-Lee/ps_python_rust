use std::cmp::Reverse;
use std::collections::HashMap;
use std::fmt::Write;
use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().lock().read_to_string(&mut buf).unwrap();
    let mut buf = buf.split_ascii_whitespace();
    let mut iterator = || buf.next().unwrap();
    let n: usize = iterator().parse::<usize>().unwrap();
    let m = iterator().parse::<usize>().unwrap();

    let mut hash: HashMap<&str, usize> = HashMap::with_capacity(n);

    for _ in 0..n {
        let key = iterator();
        if key.len() < m {
            continue;
        }
        hash.entry(key).and_modify(|v| *v += 1).or_insert(1);
    }
    let mut result: Vec<(&str, usize)> = hash.into_iter().collect();
    result.sort_by_key(|&(key, count)| (Reverse(count), Reverse(key.len()), key));
    let mut stdout = String::new();
    for word in result {
        writeln!(stdout, "{}", word.0).unwrap();
    }
    print!("{}", stdout);
}
