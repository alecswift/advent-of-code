package main

import (
	"fmt"
	"strings"

	"github.com/alecswift/advent_of_code/stringOps"
	"github.com/alecswift/advent_of_code/util"
)

func main() {
	ranges := parse("/home/alec/Desktop/code/advent-of-code/2017/day_13/input.txt")
	part1Sol, _ := part1(ranges, 0)
	part2Sol := part2(ranges)
	fmt.Print(part1Sol, "\n", part2Sol)
}

func part1(ranges [][]int, start int) (int, bool) {
	var total int
	var caught bool

	for _, data := range ranges {
		depth, fRange := data[0], data[1]

		if (depth + start) % ((fRange - 1) * 2) == 0 {
			caught = true
			total += depth * fRange
		}
	}
	return total, caught
}

func part2(ranges [][]int) int {
	var start int
	for true {
		_, caught := part1(ranges, start)

		if !caught {
			return start
		}

		start++
	}

	return -1
}


func parse(inputFile string) [][]int {
	inputData := util.FileToStr(inputFile)
	splitLines := strings.Split(inputData, "\n")
	ranges := [][]int{}

	for _, line := range splitLines {
		data := strings.Split(line, ": ")
		depth := stringOps.StrToInt(data[0])
		fRange := stringOps.StrToInt(data[1])

		ranges = append(ranges, []int{depth, fRange})
	}

	return ranges
}