package main

import (
	"fmt"
	"math"
	"strings"

	"github.com/alecswift/advent_of_code/stringOps"
	"github.com/alecswift/advent_of_code/util"
)

func main() {
	instructions := parse("/home/alec/Desktop/code/advent-of-code/2017/day_23/input.txt")
	countMul := execute(instructions)
	fmt.Print(countMul, "\n")
	fmt.Print(optimized(), "\n")
}

func optimized() int {
	var count int
	var leave bool
	
	for i := 109300; i < 126301; i += 17 {
		leave = false
		for j := 2; j < i; j++ {
			for k := 2; k <= int(math.Sqrt(float64(i))); k++ {
				if j * k == i {
					count++
					leave = true
					break
				}
			}
			if leave {
				break
			}
		}
	}

	return count
}

func execute(instructions [][]string) int {
	regs := map[string]int{"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}
	countMul := 0

	for idx := 0; idx < len(instructions); idx++ {
		instruction, ops := instructions[idx][0], instructions[idx][1:]
		
		switch instruction {
		case "set":
			reg, val := ops[0], determineVal(ops[1], regs)
			regs[reg] = val
		case "sub":
			reg, val := ops[0], determineVal(ops[1], regs)
			regs[reg] -= val
		case "mul":
			reg, val := ops[0], determineVal(ops[1], regs)
			regs[reg] *= val
			countMul++
		case "jnz":
			valX, valY := determineVal(ops[0], regs), determineVal(ops[1], regs)
			if valX != 0 {
				idx += (valY - 1)
			}
		}
	}
	return countMul
}

func determineVal(val string, regs map[string]int) int {
	out, exists := regs[val]
	if !exists {
		out = stringOps.StrToInt(val)
	}
	return out
}

func parse(inputFile string) [][]string {
	data := util.FileToStr(inputFile)
	splitLines := strings.Split(data, "\n")
	instructions := [][]string{}

	for _, line := range splitLines {
		instructions = append(instructions, strings.Split(line, " "))
	}

	return instructions
}