package main

import (
	"fmt"

	"github.com/alecswift/advent_of_code/util"
)

func main() {
	groups := util.FileToStr("/home/alec/Desktop/code/advent_of_code/2017/day_9/input.txt")
	score, ignoreChars := findScore(groups)
	fmt.Print(score, "\n", ignoreChars)
}

func findScore(groups string) (int, int) {
	var stack []rune
	var score int
	var ignoreChars int
	var ignore bool

	for i := 0; i < len(groups) ; i++ {
		char := rune(groups[i])

		if ignore && char == '!' {
			i += 1
		} else if char == '>' {
			ignore = false
		} else if ignore {
			ignoreChars++
		} else if char == '<' {
			ignore = true
		} else if char == '{' {
			stack = append(stack, char)
		} else if char == '}' {
			score += len(stack)
			stack = stack[:len(stack) - 1]
		}
	}

	return score, ignoreChars
}
