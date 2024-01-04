use std::collections::HashMap;
use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut buf_iter = buf
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>())
        .flatten();
    let n = buf_iter.next().unwrap();
    let mut cycle_table: Vec<usize> = (0..=n).collect();
    let teams: HashMap<usize, usize> = buf_iter.into_iter().enumerate().collect();
    let mut edges = Vec::new();
    for i in 0..(n - 1) {
        for j in (i + 1)..n {
            edges.push((i, j, teams.get(&i).unwrap() ^ teams.get(&j).unwrap()));
        }
    }

    edges.sort_by(|a, b| b.2.cmp(&a.2));

    let mut result = 0;

    for (start, depart, value) in edges {
        let mut parents_of_start = find_parents(&mut cycle_table, start);
        let mut parents_of_depart = find_parents(&mut cycle_table, depart);
        if parents_of_start != parents_of_depart {
            let min_parents = parents_of_start.min(parents_of_depart);
            cycle_table[parents_of_start] = min_parents;
            cycle_table[parents_of_depart] = min_parents;

            result += value
        }
    }
    println!("{}", result);
}

fn find_parents(table: &mut Vec<usize>, v: usize) -> usize {
    if v != table[v] {
        table[v] = find_parents(table, table[v]);
    }
    return table[v];
}
