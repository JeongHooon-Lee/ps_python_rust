use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut inputs = buf
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>())
        .flatten();
    let mut iterator = || inputs.next().unwrap();

    let (n, m, p) = (iterator(), iterator(), iterator());
    let mut favourite: Vec<_> = Vec::new();
    let mut hate: Vec<i64> = vec![-1; m + 1];
    let mut result = 0;
    let mut visited = vec![false; m + 1];
    let mut current_ch = p;
    visited[current_ch] = true;

    for i in 0..n {
        favourite.push(iterator());
        let inx = iterator();
        if hate[inx] == -1 {
            hate[inx] = i as i64;
        }
    }

    loop {
        let next_pensioner = hate[current_ch];
        if next_pensioner != -1 {
            let next_ch = favourite[next_pensioner as usize];
            if visited[next_ch] == true {
                result = -1;
                break;
            } else {
                visited[next_ch] = true;
                current_ch = next_ch;
                result += 1;
            }
        } else {
            break;
        }
    }
    println!("{:?}", result);
}
