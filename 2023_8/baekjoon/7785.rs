use std::collections::HashSet;
use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut iterator = buf.split_ascii_whitespace();
    let mut iterator = || iterator.next().unwrap();
    let n = iterator().parse().unwrap();
    let mut hash: HashSet<String> = HashSet::new();

    for _ in 0..n {
        let name = iterator();
        let status = iterator();
        if status == "enter" {
            hash.insert(name.to_string());
        } else {
            hash.remove(&name.to_string());
        }
    }

    let mut keys: Vec<_> = hash.into_iter().collect();
    keys.sort_by(|a, b| b.cmp(a));
    println!("{}", keys.join("\n"));
}
