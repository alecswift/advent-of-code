package main

import (
	"fmt"

	"github.com/alecswift/advent_of_code/util"
)

func main() {
	seq := parse("/home/alec/Desktop/code/advent-of-code/2018/day_05/input.txt")
	part1Sol := react(seq)
	fmt.Print(part1Sol)
}

func react(seq []rune) int {
	idx := 1

	for idx < len(seq) {
		lastIdx := len(seq) - 1
		char1, char2 := seq[idx - 1], seq[idx]
		if abs(int(char2) - int(char1)) == 32 {
            seq = append(seq[:idx - 1], seq[idx + 1:]...)
			
			if idx > 1 && idx != lastIdx {idx--}
		} else {
			idx++
		}
	}

	return len(seq)
}

func abs(num int) int {
	if num >= 0 {
		return num
	}
	return -num
}

func parse(inputFile string) []rune {
	seqStr := util.FileToStr(inputFile)
	seq := []rune{}

	for _, char := range seqStr {
		seq = append(seq, char)
	}

	return seq
}
