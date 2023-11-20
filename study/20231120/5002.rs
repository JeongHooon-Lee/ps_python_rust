use std::io::{stdin, Read};
fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let x = buf.lines().next().unwrap().parse::<i32>().unwrap();
    let mut people: Vec<char> = buf.lines().skip(1).flat_map(|line| line.chars()).collect();
    let num = people.len();
    let mut result = 0;
    let (mut M, mut W) = (0, 0);

    for i in 0..num {
        let mut n_m = M + ('M' == people[i]) as i32;
        let mut n_w = W + ('W' == people[i]) as i32;
        let t = (n_m - n_w) as i32;
        if t.abs() > x {
            if i < num - 1 {
                people.swap(i, i + 1);
            }
            n_m = M + ('M' == people[i]) as i32;
            n_w = W + ('W' == people[i]) as i32;
            let t = (n_m - n_w) as i32;
            if t.abs() > x {
                break;
            }
        }
        result += 1;
        M = n_m;
        W = n_w;
    }
    println!("{}", result);
}
