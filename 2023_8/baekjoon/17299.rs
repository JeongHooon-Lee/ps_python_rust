use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut buf = buf.split_ascii_whitespace().map(str::parse).flatten();
    let n = buf.next().unwrap();
    let mut freq = vec![0; 1_000_001];
    let arr: Vec<usize> = buf.take(n).inspect(|v| freq[*v] += 1).collect();
    let mut stack: Vec<usize> = vec![0];
    let mut result: Vec<i32> = vec![-1; n];

    for i in 0..n {
        while !stack.is_empty() && freq[arr[*stack.last().unwrap()]] < freq[arr[i]] {
            result[stack.pop().unwrap()] = arr[i] as i32;
        }
        stack.push(i);
    }
    println!(
        "{}",
        result
            .iter()
            .map(|v| v.to_string())
            .collect::<Vec<String>>()
            .join(" ")
    );
}
