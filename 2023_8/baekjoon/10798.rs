use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut arr: Vec<String> = vec![String::new(); 15];

    buf.lines().for_each(|line| {
        line.chars().enumerate().for_each(|(index, value)| {
            arr[index].push(value);
        });
    });

    // for line in buf.lines() {
    //     let chars: Vec<char> = line.chars().collect();
    //     for (index, value) in chars.iter().enumerate() {
    //         arr[index].push(*value);
    //     }
    // }

    println!("{}", arr.concat());
}
