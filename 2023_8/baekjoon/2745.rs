use std::io::stdin;

fn main() {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();
    let mut buf = buf.split_ascii_whitespace();
    let n = buf.next().unwrap();
    let b: u32 = buf.next().unwrap().parse().unwrap();

    println!("{}", i32::from_str_radix(n, b).unwrap());
}

// use std::collections::HashMap;
// use std::io::{stdin, Read};

// fn initialize_hash() -> HashMap<char, u32> {
//     let mut map: HashMap<char, u32> = HashMap::new();
//     for i in 0..10 {
//         map.insert(char::from_u32(i + 48).unwrap(), i);
//     }
//     for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ".chars() {
//         map.insert(ch, ch as u32 - 55);
//     }
//     map
// }

// fn main() {
//     let mut buf = String::new();
//     stdin().read_to_string(&mut buf).unwrap();
//     let mut iterator = buf.split_ascii_whitespace();
//     let n = iterator.next().unwrap();
//     let b = iterator.next().unwrap().parse::<u32>().unwrap();

//     let map = initialize_hash();
//     let mut answer: u32 = 0;

//     for i in 0..n.len() {
//         answer += b.pow((n.len() - 1 - i) as u32) * map[&n.chars().nth(i).unwrap()];
//     }

//     println!("{}", answer);
// }
