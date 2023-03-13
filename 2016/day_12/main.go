// Puzzle Explanation: https://adventofcode.com/2016/day/12

package main

import (
	"fmt"
	"os"
	"strings"
	"strconv"
)

func main() {
	instructions := parse("2016/day_12/input.txt")
	part1Solution := execute(instructions, 0)
	fmt.Print(part1Solution, "\n")
	part2Solution := execute(instructions, 1)
	fmt.Print(part2Solution)
}

func parse(input_file string) [][]string {
	input_data, err := os.ReadFile(input_file)
	if err != nil {
		panic("Error")
	}
	split_lines := strings.Split(string(input_data), "\n")
	var out [][]string
	for _, line := range split_lines {
		out = append(out, strings.Split(line, ` `))
	}
	return out
}

func execute(instructions [][]string, registerC int) int {
	registers := map[string]int{"a": 0, "b": 0, "c": registerC, "d": 0}
	idx :=0
	for idx  < len(instructions) {
		line := instructions[idx]
		instruction := line[0]
		switch instruction {
		case "cpy":
			reg := line[2]
			operand, err := strconv.Atoi(line[1])
			if err != nil {
				registers[reg] = registers[line[1]]
			} else {
				registers[reg] = operand
			}
			idx++
		case "inc":
			reg := line[1]
			registers[reg]++
			idx++
		case "dec":
			reg := line[1]
			registers[reg]--
			idx++
		case "jnz":
			jmp, err := strconv.Atoi(line[2])
			if err != nil {
				panic("Error")
			}
			operand, err := strconv.Atoi(line[1])
			if err != nil {
				if registers[line[1]] != 0 {
					idx += jmp
				} else {
					idx++
				}
			} else {
				if operand != 0 {
					idx += jmp
				} else {
					idx++
				}
			}
		}
	}
	return registers["a"]
}