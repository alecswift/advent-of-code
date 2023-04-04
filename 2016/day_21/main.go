// Puzzle Explanation: https://adventofcode.com/2016/day/21

package main

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"

	"github.com/alecswift/advent_of_code/arrayOps"
	"github.com/alecswift/advent_of_code/util"
)

func main() {
	password := "abcdefgh"
	seq := strings.Split(password, "")
	instructions := parse("/home/alec/Desktop/code/advent-of-code/2016/day_21/input.txt")
	scrambled := scramble(seq, instructions)
	fmt.Print(scrambled, "\n")
	part2scrambled := "fbgdceah"
	seq2 := strings.Split(part2scrambled, "")
	unscrambled := unscramble(seq2, instructions)
	fmt.Print(unscrambled)

}

func parse(inputFile string) [][]string {
	inputData := util.FileToStr(inputFile)
	split_lines := strings.Split(inputData, "\n")
	instructions := [][]string{}
	for _, line := range split_lines {
		pat := `(^[a-z]+)|(right)|(left)|(\d+)|( [a-z] )|( [a-z]$)`
		re := regexp.MustCompile(pat)
		instruction := re.FindAllString(line, -1)
		instructions = append(instructions, instruction)
	}
	return instructions
}

func scramble(seq []string, instructions [][]string) string {
	for _, instruction := range instructions {
		switch instruction[0] {
		case "rotate":
			var steps int
			var direction int

			if len(instruction) == 2 {
				letter := strings.Trim(instruction[1], " ")
				steps = determineRotations(seq, letter)
				seq = arrayOps.Rotate(seq, steps, 1)
			} else {
				steps = strToNum(instruction[2])
				if instruction[1] == "right" {
					direction = 1
				} else {
					direction = -1
				}
				seq = arrayOps.Rotate(seq, steps, direction)
			}

		case "swap":
			if isDigit(instruction[1]) {
				idx1, idx2 := strToNum(instruction[1]), strToNum(instruction[2])
				swap(seq, idx1, idx2)
			} else {
				letter1 := strings.Trim(instruction[1], " ")
				letter2 := strings.Trim(instruction[2], " ")
				idx1, idx2 := search(seq, letter1), search(seq, letter2)
				swap(seq, idx1, idx2)
			}

		case "reverse":
			start, end := strToNum(instruction[1]), strToNum(instruction[2])
			arrayOps.ReverseFrom(seq, start, end)
		case "move":
			idx1, idx2 := strToNum(instruction[1]), strToNum(instruction[2])
			move(seq, idx1, idx2)
		}
	}
	return strings.Join(seq, "")
}

func unscramble(seq []string, instructions [][]string) string {
	for i := len(instructions) - 1; -1 < i; i-- {
		instruction := instructions[i]
		switch instruction[0] {
		case "rotate":
			var steps int
			var direction int

			if len(instruction) == 2 {
				letter := strings.Trim(instruction[1], " ")
				steps = determineRotationsRev(seq, letter)
				seq = arrayOps.Rotate(seq, steps, -1)
			} else {
				steps = strToNum(instruction[2])
				if instruction[1] == "right" {
					direction = -1
				} else {
					direction = 1
				}
				seq = arrayOps.Rotate(seq, steps, direction)
			}

		case "swap":
			if isDigit(instruction[1]) {
				idx1, idx2 := strToNum(instruction[1]), strToNum(instruction[2])
				swap(seq, idx1, idx2)
			} else {
				letter1 := strings.Trim(instruction[1], " ")
				letter2 := strings.Trim(instruction[2], " ")
				idx1, idx2 := search(seq, letter1), search(seq, letter2)
				swap(seq, idx1, idx2)
			}

		case "reverse":
			start, end := strToNum(instruction[1]), strToNum(instruction[2])
			arrayOps.ReverseFrom(seq, start, end)
		case "move":
			idx2, idx1 := strToNum(instruction[1]), strToNum(instruction[2])
			move(seq, idx1, idx2)
		}
	}
	return strings.Join(seq, "")
}

func strToNum(numStr string) int {
	num, err := strconv.Atoi(numStr)
	if err != nil {
		panic(err)
	}
	return num
}

func isDigit(char string) bool {
	digits := map[string]int{"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
	_, exists := digits[char]
	return exists
}

func search(seq []string, letter string) int {
	for idx, char := range seq {
		if char == letter {
			return idx
		}
	}
	return -1
}

func swap(seq []string, idx1, idx2 int) {
	seq[idx1], seq[idx2] = seq[idx2], seq[idx1]
}

func determineRotations(seq []string, letter string) int {
	idx := search(seq, letter)
	if 4 <= idx {
		idx++
	}
	return idx + 1
}

func determineRotationsRev(seq []string, letter string) int {
	idxToSteps := map[int]int{0: 1, 1: 1, 2: 6, 3: 2, 4: 7, 5: 3, 6: 8, 7: 4}
	idx := search(seq, letter)
	return idxToSteps[idx]
}

func move(seq []string, idx1, idx2 int) {
	letter := seq[idx1]
	seq = append(seq[0:idx1], seq[idx1+1:]...)
	right := make([]string, len(seq)-idx2)
	copy(right, seq[idx2:])
	seq = append(seq[:idx2], letter)
	seq = append(seq, right...)
}
