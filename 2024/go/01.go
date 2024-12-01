package main

import (
	"bytes"
	"fmt"
	"io"
	"os"
	"sort"
	"strconv"
)

func main() {
	if err := mainImpl(); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}

func mainImpl() error {
	input, err := io.ReadAll(os.Stdin)
	if err != nil {
		return fmt.Errorf("error reading input: %w", err)
	}

	listA, listB, err := parseInput(bytes.TrimSpace(input))
	if err != nil {
		return fmt.Errorf("error parsing input: %w", err)
	}

	sort.Ints(listA)
	sort.Ints(listB)

	part1 := 0
	for i := range listA {
		part1 += abs(listA[i] - listB[i])
	}
	fmt.Printf("Part 1: %d\n", part1)

	counts := map[int]int{}
	for _, b := range listB {
		counts[b]++
	}
	part2 := 0
	for _, a := range listA {
		part2 += a * counts[a]
	}
	fmt.Printf("Part 2: %d\n", part2)

	return nil
}

func parseInput(data []byte) ([]int, []int, error) {
	var listA, listB []int
	for _, line := range bytes.Split(data, []byte("\n")) {
		vals := bytes.Fields(line)
		if len(vals) != 2 {
			return nil, nil, fmt.Errorf("invalid input line (expected 2 values): %q", string(line))
		}
		a, err := strconv.Atoi(string(vals[0]))
		if err != nil {
			return nil, nil, fmt.Errorf("error parsing first value of %q: %w", string(line), err)
		}
		b, err := strconv.Atoi(string(vals[1]))
		if err != nil {
			return nil, nil, fmt.Errorf("error parsing second value of %q: %w", string(line), err)
		}
		listA = append(listA, a)
		listB = append(listB, b)
	}
	return listA, listB, nil
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
