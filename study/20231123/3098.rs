use std::collections::HashSet;
use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut buf = buf
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>())
        .flatten();
    let mut iterator = || buf.next().unwrap();

    let (n, m) = (iterator(), iterator());
    let mut relations: Vec<HashSet<usize>> = vec![HashSet::new(); n + 1];
    for i in 1..=n {
        relations[i].insert(i);
    }

    for _i in 0..m {
        let a = iterator();
        let b = iterator();
        relations[a].insert(b);
        relations[b].insert(a);
    }
    solution(relations, n);
}

fn is_finish(relations: &Vec<HashSet<usize>>, n: usize) -> bool {
    for i in 1..=n {
        if relations[i].len() != n {
            return false;
        }
    }
    true
}

fn solution(mut relations: Vec<HashSet<usize>>, n: usize) {
    let mut result = 0;
    let mut relations_count: Vec<usize> = Vec::new();
    loop {
        let mut today_created = 0;
        if is_finish(&relations, n) {
            break;
        }

        let mut new_relations: Vec<HashSet<usize>> = vec![HashSet::new(); n + 1];
        for i in 1..=n {
            for friend in &relations[i] {
                new_relations[i].extend(&relations[*friend]);
            }
        }

        for i in 1..=n {
            let temp = relations[i].len();
            relations[i].extend(&new_relations[i]);
            today_created += relations[i].len() - temp
        }
        relations_count.push(today_created / 2);
        result += 1;
    }
    println!("{}", result);
    for i in relations_count {
        println!("{}", i);
    }
}
