use std::iter::zip;

fn main() {
    let input: Vec<(i32, i32)> = std::io::stdin().lines().map(parse_line).collect();
    let mut list_a: Vec<i32> = input.iter().map(|(a, _)| *a).collect();
    let mut list_b: Vec<i32> = input.iter().map(|(_, b)| *b).collect();
    list_a.sort();
    list_b.sort();
    let part1: i32 = zip(&list_a, &list_b).map(|(a, b)| (a - b).abs()).sum();
    println!("Part 1: {part1}");

    let b_counts = list_b
        .iter()
        .fold(std::collections::HashMap::new(), |mut acc, b| {
            *acc.entry(b).or_insert(0) += 1;
            acc
        });
    let part2: i32 = list_a
        .iter()
        .map(|a| a * b_counts.get(a).unwrap_or(&0))
        .sum();
    println!("Part 2: {part2}");
}

fn parse_line(line: std::io::Result<String>) -> (i32, i32) {
    let line = line.unwrap();
    let mut iter = line.split_whitespace();
    let a: i32 = iter.next().unwrap().parse().unwrap();
    let b: i32 = iter.next().unwrap().parse().unwrap();
    (a, b)
}
