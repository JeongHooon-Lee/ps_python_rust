use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut papers: Vec<i32> = buf
        .split_ascii_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
    let mut result = 0;

    for i in 2..6 {
        match i {
            2 => {
                let t = (papers[i] as f64 / 4.0).ceil() as i32;
                result += t;
                let rem = papers[i] % 4;
                match rem {
                    0 => {}
                    1 | 2 | 3 => {
                        papers[0] -= 8 - rem;
                        papers[1] -= 7 - 2 * rem;
                    }
                    _ => unreachable!(),
                }
            }
            3 => {
                result += papers[i];
                papers[1] -= papers[i] * 5;
            }
            4 => {
                result += papers[i];
                papers[0] -= papers[i] * 11;
            }
            5 => result += papers[i],
            _ => unreachable!(),
        }
    }
    if papers[1] > 0 {
        let t = (papers[1] as f64 / 9.0).ceil() as i32;
        result += t;
        papers[1] -= t * 9;
    }
    if papers[0] > 0 {
        if papers[0] > papers[1].abs() * 4 {
            result += ((papers[0] - papers[1].abs() * 4) as f64 / 36.0).ceil() as i32;
        }
    }
    println!("{:?}", result);
}
