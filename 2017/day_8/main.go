package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/alecswift/advent_of_code/arrayOps"
	"github.com/alecswift/advent_of_code/util"
)
func main() {
	instructions, regs := parse("/home/alec/Desktop/code/advent_of_code/2017/day_8/input.txt")

	newRegs, maxRegNum := execute(instructions, regs)
	maxNum := findMaxReg(newRegs)
	fmt.Print(maxNum, "\n", maxRegNum)
	
}

func findMaxReg(regs map[string]int) int {
	firstHit := true
	var maxNum int
	for _, val := range regs {
		if firstHit {
			maxNum = val
			firstHit = false
		} else if val > maxNum {
			maxNum = val
		}
	}

	return maxNum
}

func execute(instructions [][]string, regs map[string]int) (map[string]int, int) {
	maxRegNum := 0

	for _, instr := range instructions {
		reg, op := instr[0], instr[1]
		cmprReg, cmprOp := instr[4], instr[5]
		num := strToNum(instr[2])
		cmprNum := strToNum(instr[3])

		conditionTrue := boolOps(regs[cmprReg], cmprNum, cmprOp)
		
		if conditionTrue {
			newRegNum := arithOps(regs[reg], num, op)
			regs[reg] = newRegNum
			if newRegNum > maxRegNum {
				maxRegNum = newRegNum
			}
		}
	}

	return regs, maxRegNum
}

func arithOps(num1, num2 int, operator string) int {
	switch operator {
	case "inc":
		return num1 + num2
	case "dec":
		return num1 - num2
	}

	panic("Not a valid operator")
}

func boolOps(num1, num2 int, operator string) bool {
	switch operator {
	case "<":
		return num1 < num2
	case ">":
		return num1 > num2
	case "<=":
		return num1 <= num2
	case ">=":
		return num1 >= num2
	case "==":
		return num1 == num2
	case "!=":
		return num1 != num2
	}

	panic("Not a valid operator")
}

func parse(inputFile string) ([][]string, map[string]int) {
	inputData := util.FileToStr(inputFile)
	splitLines := strings.Split(inputData, "\n")
	var instructions [][]string
	regs := make(map[string]int)

	for _, line := range splitLines {
		splitSpace := strings.Split(line, " ")
		splitSpace = arrayOps.Remove(splitSpace, 3)
		// reg1, instr, instrNum, cmprNum, cmprReg, cmprOp
		instructions = append(instructions, splitSpace)
		regs[splitSpace[0]] = 0
		regs[splitSpace[4]] = 0
	}

	return instructions, regs
}

func strToNum(strNum string) int {
	num, err := strconv.Atoi(strNum)

	if err != nil {
		panic(err)
	}

	return num
}