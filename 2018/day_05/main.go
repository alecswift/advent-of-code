// Puzzle explanation: https://adventofcode.com/2018/day/5

package main

import (
	"fmt"

	"github.com/alecswift/advent_of_code/util"
)

func main() {
	seq := parse("/home/alec/Desktop/code/advent-of-code/2018/day_05/input.txt")
	part1Sol := react(seq)
	seq2 := parse("/home/alec/Desktop/code/advent-of-code/2018/day_05/input.txt")
	part2Sol := part2(seq2)
	fmt.Print(part1Sol, "\n", part2Sol)
}

func part2(seq []rune) int {
	var min int

	for i := 65; i < 98; i++ {
		newSeq := removeChars(seq, rune(i), rune(i + 32))
		length := react(newSeq)
		if i == 65 || min > length {
			min = length
		}
	}

	return min
}

func removeChars(seq []rune, char1, char2 rune) []rune {
	out := make([]rune, len(seq))
	copy(out, seq)

	for i := 0; i < len(out); i++ {
		if out[i] == char1 || out[i] == char2 {
			out = append(out[:i], out[i + 1:]...)
			i--
		}
	}

	return out
}

func react(seq []rune) int {
	stack := []rune{}

	for _, char := range seq {
		if len(stack) == 0 {
			stack = append(stack, char)
		} else {
			stack = append(stack, char)
			char1, char2 := stack[len(stack) - 1], stack[len(stack) - 2]

			if char2 ^ char1 == 32 {
				stack = stack[:len(stack) - 2]
			}
		}
	}

	return len(stack)
}

func parse(inputFile string) []rune {
	seqStr := util.FileToStr(inputFile)
	seq := []rune{}

	for _, char := range seqStr {
		seq = append(seq, char)
	}

	return seq
}
