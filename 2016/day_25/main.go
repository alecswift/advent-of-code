package main

import (
	"fmt"
	"reflect"
	"strconv"
	"strings"

	"github.com/alecswift/advent_of_code/util"
)
func main() {
	instructions := parse("/home/alec/Desktop/code/advent_of_code/2016/day_25/input.txt")
	registerA := 0
	expected := []int{0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1}
	out := execute(instructions, registerA)
	for !reflect.DeepEqual(expected, out) {
		registerA++
		out = execute(instructions, registerA)
		// fmt.Print(out)
	}
	fmt.Print(registerA)
}

func parse(inputFile string) [][]string {
	inputData := util.FileToStr(inputFile)
	splitLines := strings.Split(string(inputData), "\n")
	var out [][]string
	for _, line := range splitLines {
		out = append(out, strings.Split(line, ` `))
	}
	return out
}

func execute(instructions [][]string, registerA int) []int {
	registers := map[string]int{"a": registerA, "b": 0, "c": 0, "d": 0}
	idx :=0
	output := []int{}
	hits := 0
	for hits < 40 {
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
		case "out":
			reg := line[1]
			output = append(output, registers[reg])
			hits += 1
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
	return output
}