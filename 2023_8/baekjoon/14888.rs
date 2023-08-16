use std::io::{stdin, Read};

struct Res {
    max: i32,
    min: i32,
}

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let lines: Vec<Vec<_>> = buf
        .lines()
        .map(|line| {
            line.split_ascii_whitespace()
                .map(|v| v.parse::<usize>().unwrap())
                .collect::<Vec<usize>>()
        })
        .collect();
    let mut res = Res {
        max: -1_000_000_000,
        min: 1_000_000_000,
    };
    back(lines[1][0] as i32, 0, &lines[1], &lines[2], &mut res);
    println!("{}\n{}", res.max, res.min);
}

fn back(values: i32, count: usize, nums: &Vec<usize>, ops: &Vec<usize>, res: &mut Res) {
    if ops.iter().sum::<usize>() == 0 {
        res.max = res.max.max(values);
        res.min = res.min.min(values);
        return;
    }

    for i in 0..4 {
        if ops[i] > 0 {
            let mut new_ops = ops.to_vec();
            new_ops[i] -= 1;
            let new_value = match i {
                0 => values + nums[count + 1] as i32,
                1 => values - nums[count + 1] as i32,
                2 => values * nums[count + 1] as i32,
                3 if values >= 0 => values / nums[count + 1] as i32,
                3 if values < 0 => -((-values) / nums[count + 1] as i32),
                _ => unreachable!(),
            };
            back(new_value, count + 1, nums, &new_ops, res);
        }
    }
}
