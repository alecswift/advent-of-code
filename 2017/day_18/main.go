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
	part1Sol, _ := execute(instructions, registers, []int{}, 0, true)
	fmt.Print(part1Sol[len(part1Sol) - 1], "\n")

	sendCount := sync(instructions, registers)
	fmt.Print(sendCount)
}

func execute(instructions [][]string, registers map[string]int, queue []int, idx int, part1 bool) ([]int, int) {

	for ;idx < len(instructions); idx++ {
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
			if part1 && val != 0 { return queue, idx
				} else { return queue, idx}
		case "jgz":
			condVal, jmpVal := determineVal(instr[1], registers), determineVal(instr[2], registers)
			if condVal > 0 {idx += jmpVal - 1}
		}
	}
	return queue, -1
}

func sync(instructions [][]string, registers1 map[string]int) int {
	var queue1, queue2 []int
	var idx1, idx2, sendCount int
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
		queue1, idx1 = execute(instructions, registers1, queue1, idx1, false)
		queue2, idx2 = execute(instructions, registers2, queue2, idx2, false)

		if len(queue1) != 0 {
			sentVal1 := queue1[0]
			rcvReg2 := instructions[idx2][1]
			registers2[rcvReg2] = sentVal1
			queue1 = queue1[1:]
			idx2++
		}
		if len(queue2) != 0 {
			sentVal2 := queue2[0]
			rcvReg1 := instructions[idx1][1]
			registers1[rcvReg1] = sentVal2
			idx1++
			sendCount++
			queue2 = queue2[1:]	
		}
		if len(queue1) == 0 && len(queue2) == 0 {
			break
		}
 	}

	return sendCount
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