// Puzzle explanation: https://adventofcode.com/2017/day/9

package main

import (
	"fmt"

	"github.com/alecswift/advent_of_code/util"
)

func main() {
	groups := util.FileToStr("/home/alec/Desktop/code/advent_of_code/2017/day_9/input.txt")
	part1, part2 := solutions(groups)
	fmt.Print(part1, "\n", part2)
}

func solutions(groups string) (int, int) {
	var stack []rune
	var score int
	var ignoreChars int
	var ignore bool

	for i := 0; i < len(groups) ; i++ {
		char := rune(groups[i])

		if ignore && char == '!' {
			i++
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
