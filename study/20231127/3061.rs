use std::io::stdin;

fn main() {
    for _ in 0..read_one_number() {
        let N = read_one_number();
        let arr = read_array();
        let mut result = 0;
        let mut values: Vec<_> = (1..=N).collect();

        for index in 0..N {
            let target = arr[index];
            let target_index = values.iter().position(|&x| x == target).unwrap();
            result += target_index;
            values.remove(target_index);
        }
        println!("{}", result);
    }
}

fn read_one_number() -> usize {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();
    let t = buf.trim().parse::<usize>().unwrap();
    t
}

fn read_array() -> Vec<usize> {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();
    buf.split_ascii_whitespace()
        .map(|x| x.parse())
        .flatten()
        .collect()
}
