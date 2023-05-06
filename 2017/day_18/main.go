// Puzzle explanation: https://adventofcode.com/2017/day/18

package main

import (
	"fmt"
	"regexp"
	"strings"

	"github.com/alecswift/advent_of_code/util"
	"github.com/alecswift/advent_of_code/stringOps"
)


// state: next instruction, registers, queue
// Go til both programs hit a rcv. Then exit input the correct que # into the rcv regs and repeat
// while loop continue until a program hits a recieve with no val in queue terminate that one
// fully end when both programs have terminated

func main() {
	instructions, registers := parse("/home/alec/Desktop/code/advent-of-code/2017/day_18/input.txt")
	part1Sol := execute(instructions, registers, []int{})
	fmt.Print(part1Sol[len(part1Sol) - 1])

	sync(instructions, registers)
}

func execute(instructions [][]string, registers map[string]int, queue []int) []int {

	for idx := 0; idx < len(instructions); idx++ {
		instr := instructions[idx]
		instrName := instr[0]

		switch instrName {
		case "snd":
			queue = append(queue, determineVal(instr[1], registers))
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
			if val != 0 {return queue}
		case "jgz":
			condVal, jmpVal := determineVal(instr[1], registers), determineVal(instr[2], registers)
			if condVal > 0 {idx += jmpVal - 1}
		}
	}
	return queue
}

func sync(instructions [][]string, registers1 map[string]int) {
	//queue1 := []int{}
	//queue2 := []int{}
	registers2 := make(map[string]int)

	for reg := range registers1 {
		registers1[reg] = 0
		if reg == "p" {
			registers2[reg] = 1
		} else {
			registers2[reg] = 0
		}
	}

	for true {

	}
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