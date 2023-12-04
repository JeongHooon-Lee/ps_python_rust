use std::io::{stdin, Read};

fn main() {
    while let Some(board) = load_map() {
        let (x_win, o_win) = win_check(&board);
        let x_count = board.iter().filter(|&x| *x == 'X').count();
        let o_count = board.iter().filter(|&x| *x == 'O').count();
        if x_win + o_win == 0 {
            if x_count + o_count == 9 && x_count == o_count + 1 {
                println!("valid");
            } else {
                println!("invalid");
            }
        } else if x_win + o_win == 1 {
            if (x_win == 1 && x_count == o_count + 1) || (o_win == 1 && x_count == o_count) {
                println!("valid");
            } else {
                println!("invalid");
            }
        } else if x_win == 2 && x_count + o_count == 9 {
            println!("valid");
        } else {
            println!("invalid");
        }
    }
}

fn win_check(board: &Vec<char>) -> (usize, usize) {
    let indexs = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ];
    let (mut x_win, mut o_win) = (0, 0);
    for [i, j, k] in indexs {
        if board[i] == board[j] && board[j] == board[k] {
            match board[i] {
                'X' => x_win += 1,
                'O' => o_win += 1,
                '.' => continue,
                _ => unreachable!(),
            }
        }
    }
    (x_win, o_win)
}

fn load_map() -> Option<Vec<char>> {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();
    match buf.trim() {
        "end" => None,
        _ => Some(buf.chars().collect()),
    }
}
