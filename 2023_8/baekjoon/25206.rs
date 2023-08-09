use std::collections::HashMap;
use std::io::{stdin, Read};

fn initialize_hash(scores: &mut HashMap<String, f32>) {
    scores.insert(String::from("A+"), 4.5);
    scores.insert(String::from("B+"), 3.5);
    scores.insert(String::from("C+"), 2.5);
    scores.insert(String::from("D+"), 1.5);
    scores.insert(String::from("A0"), 4.0);
    scores.insert(String::from("B0"), 3.0);
    scores.insert(String::from("C0"), 2.0);
    scores.insert(String::from("D0"), 1.0);
    scores.insert(String::from("F"), 0.0);
}

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut iterator = buf.split_whitespace();
    let mut iterator = || iterator.next().unwrap();

    let mut scores: HashMap<String, f32> = HashMap::new();
    initialize_hash(&mut scores);

    let mut total_units: f32 = 0.0f32;
    let mut total_scores: f32 = 0.0f32;
    for _ in buf.lines() {
        let _ = iterator();
        let unit = iterator().parse::<f32>().unwrap();
        let score = iterator();
        if score == "P" {
            continue;
        }
        total_units += unit;
        total_scores += unit * scores[&score.to_string()];
    }
    println!("{}", total_scores / total_units);
    return;
}
