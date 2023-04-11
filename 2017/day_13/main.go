package main

import (
	"fmt"
	"strings"

	"github.com/alecswift/advent_of_code/stringOps"
	"github.com/alecswift/advent_of_code/util"
)

func main() {
	part1 := parse("/home/alec/Desktop/code/advent-of-code/2017/day_13/input.txt")
	fmt.Print(part1)
}


func parse(inputFile string) int {
	inputData := util.FileToStr(inputFile)
	splitLines := strings.Split(inputData, "\n")
	total := 0

	for _, line := range splitLines {
		data := strings.Split(line, ": ")
		depth := stringOps.StrToInt(data[0])
		fRange := stringOps.StrToInt(data[1])

		if depth % ((fRange - 1) * 2) == 0 {
			total += depth * fRange
		}
	}

	return total
}