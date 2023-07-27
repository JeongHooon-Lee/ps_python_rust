use std::cmp;
use std::io::{stdin, Read};

fn main() {
    let mut input = String::new();
    stdin().read_to_string(&mut input).unwrap();
    let mut itera = input.split_ascii_whitespace();
    let mut iterator = || itera.next().unwrap();
    let t = iterator().parse::<usize>().unwrap();

    for _ in 0..t {
        let n = iterator().parse::<usize>().unwrap();
        if n >= 48 {
            println!("0");
            for _ in 0..n {
                iterator();
            }
            continue;
        }

        let mut mbti_list = vec![];
        for _ in 0..n {
            let mut mbti = ['\0'; 4];
            for (i, ch) in iterator().chars().enumerate() {
                mbti[i] = ch;
            }
            mbti_list.push(mbti);
        }

        let mut _result = usize::MAX;
        for a in 0..n {
            for b in (a + 1)..n {
                for c in (b + 1)..n {
                    let dst = {
                        (0..4).fold(0, |acc, x| {
                            acc + (mbti_list[a][x] != mbti_list[b][x]) as usize
                        }) + (0..4).fold(0, |acc, x| {
                            acc + (mbti_list[b][x] != mbti_list[c][x]) as usize
                        }) + (0..4).fold(0, |acc, x| {
                            acc + (mbti_list[a][x] != mbti_list[c][x]) as usize
                        })
                    };
                    if dst < _result {
                        _result = dst
                    }
                }
            }
        }
        println!("{}", _result);
    }
}
