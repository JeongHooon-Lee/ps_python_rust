use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut buf: Vec<_> = buf
        .lines()
        .map(|line| {
            line.split_ascii_whitespace()
                .map(|x| x.parse::<i32>().unwrap())
                .collect::<Vec<i32>>()
        })
        .collect();

    let k = buf[0][1];
    let mut array = buf.remove(1);
    let n = array.len();

    let k = merge_sort(&mut array, 0, n - 1, k);
    if k > 0 {
        println!("-1");
    }
}

fn merge_sort(arr: &mut Vec<i32>, p: usize, r: usize, mut k: i32) -> i32 {
    if p < r {
        let q = (p + r) / 2 as usize;
        k = merge_sort(arr, p, q, k);
        k = merge_sort(arr, q + 1, r, k);
        k = merge(arr, p, q, r, k);
    }
    k
}

fn merge(arr: &mut Vec<i32>, p: usize, q: usize, r: usize, mut k: i32) -> i32 {
    let mut i = p;
    let mut j = q + 1;
    let mut t = 0;
    let mut temp: Vec<i32> = Vec::new();

    while i <= q && j <= r {
        if arr[i] <= arr[j] {
            temp.push(arr[i]);
            i += 1;
        } else {
            temp.push(arr[j]);
            j += 1;
        }
        t += 1;
    }

    while i <= q {
        temp.push(arr[i]);
        i += 1;
    }
    while j <= r {
        temp.push(arr[j]);
        j += 1;
    }
    i = p;
    t = 0;

    while i <= r {
        arr[i] = temp[t];
        k -= 1;
        if k == 0 {
            println!("{}", arr[i]);
            break;
        }
        i += 1;
        t += 1;
    }
    k
}
