// Puzzle explanation: https://adventofcode.com/2017/day/17

package main

import (
	"fmt"

	"github.com/alecswift/advent_of_code/arrayOps"
)

const Steps = 363

func main() {
	initialBuffer := []int{0}
	part1Sol := part1(initialBuffer)
	fmt.Print(part1Sol, "\n")

	part2Sol := part2()
	fmt.Print(part2Sol)
}	

func part1(buffer []int) int {
	var currPos int

	for i := 1; i <= 2017; i++ {
		currPos = (currPos + Steps) % len(buffer)
		currPos++
		buffer = arrayOps.Insert(buffer, currPos, i)
	}

	return buffer[currPos + 1]
}

func part2() int {
	var currPos int
	var zeroPos int
	var valAfterZero int

	for i := 1; i <= 50000000; i++ {
		currPos = (currPos + Steps) % i
		currPos++

		if currPos == zeroPos + 1 {
			valAfterZero = i
		}
		if currPos <= zeroPos {
			zeroPos++
		}
	}

	return valAfterZero
}