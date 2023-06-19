package main

import (
	"fmt"
)

func main() {
	const InitialState = "A"
	const Steps = 12667664
	blueprint := map[string][2][3]int{
		"A": {{1, 1, 66}, {0, -1, 67}},
		"B": {{1, -1, 65}, {1, 1, 68}},
		"C": {{0, -1, 66}, {0, -1, 69}},
		"D": {{1, 1, 65}, {0, 1, 66}},
		"E": {{1, -1, 70}, {1, -1, 67}},
		"F": {{1, 1, 68}, {1, 1, 65}},
	}
	tape := run(blueprint, InitialState, Steps)
	set := countSet(tape)
	fmt.Print(set)
}

func run(blueprint map[string][2][3]int, state string, steps int) map[int]int {
	tape := make(map[int]int)
	pos := 0

	for i := 0; i < steps; i++ {
		val, _ := tape[pos]
		instructions := blueprint[state][val]
		newVal, dir := instructions[0], instructions[1]

		tape[pos] = newVal
		pos += dir
		state = string(instructions[2])
	}

	return tape
}

func countSet(tape map[int]int) int {
	count := 0

	for _, bit := range tape {
		count += bit
	}

	return count
}