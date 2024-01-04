use std::collections::VecDeque;
use std::io::stdin;

fn main() {
    while let Some(n) = get_input() {
        let temp = String::from('1');
        let mut queue = VecDeque::new();
        queue.push_back(temp);

        while let Some(v) = queue.pop_front() {
            let values = v.parse::<i128>().unwrap();

            if values % n as i128 == 0 {
                println!("{}", values);
                break;
            }

            for c in ['0', '1'] {
                let mut next_string = v.clone();
                next_string.push(c);
                queue.push_back(next_string);
            }
        }
    }
}

fn get_input() -> Option<i32> {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();

    match buf.trim() {
        "0" => None,
        v => Some(v.parse::<i32>().unwrap()),
    }
}
