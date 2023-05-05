package main

import (
	"fmt"
	"regexp"
	"strings"

	"github.com/alecswift/advent_of_code/util"
	"github.com/alecswift/advent_of_code/stringOps"
)

func main() {
	instructions, registers := parse("/home/alec/Desktop/code/advent-of-code/2017/day_18/input.txt")
	part1Sol := execute(instructions, registers)
	fmt.Print(part1Sol)


}

func execute(instructions [][]string, registers map[string]int) int {
	var prevFreq int

	for idx := 0; idx < len(instructions); idx++ {
		instr := instructions[idx]
		instrName := instr[0]

		switch instrName {
		case "snd":
			prevFreq = determineVal(instr[1], registers)
		case "set":
			reg, val := instr[1], determineVal(instr[2], registers)
			registers[reg] = val
		case "add":
			reg, val := instr[1], determineVal(instr[2], registers)
			registers[reg] += val
		case "mul":
			reg, val := instr[1], determineVal(instr[2], registers)
			registers[reg] *= val
		case "mod":
			reg, val := instr[1], determineVal(instr[2], registers)
			registers[reg] %= val
		case "rcv":
			val := determineVal(instr[1], registers)
			if val == 0 {continue}
			return prevFreq
		case "jgz":
			condVal, jmpVal := determineVal(instr[1], registers), determineVal(instr[2], registers)
			if condVal <= 0 {continue}
			idx += jmpVal - 1
		}
	}
	return -1
}

func determineVal(char string, registers map[string]int) int {
	val, exists := registers[char]

	if !exists {
		val = stringOps.StrToInt(char)
	}

	return val
}

func parse(inputFile string) ([][]string, map[string]int) {
	inputData := util.FileToStr("/home/alec/Desktop/code/advent-of-code/2017/day_18/input.txt")
	splitLines := strings.Split(inputData, "\n")
	instructions := make([][]string, len(splitLines))

	for idx, line := range splitLines {
		instructions[idx] = strings.Split(line, " ")
	}

	re := regexp.MustCompile(` [a-z]`)
	regNames := re.FindAllString(inputData, -1)
	registers := make(map[string]int)

	for _, name := range regNames {
		registers[name[1:]] = 0
	}

	return instructions, registers
}