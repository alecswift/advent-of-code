// https://adventofcode.com/2023/day/2

package main

import (
	"fmt"
	"strings"

	"github.com/alecswift/advent_of_code/util"
)

func main() {
	data := util.FileToStr("/home/alec/Desktop/code/advent-of-code/2023/day_03/input.txt")
	grid := parse(data)
	fmt.Print(grid)
}

func part1(grid [][]rune) {

	for rowNum, row := range grid {
		for colNum, val := range grid {
			
		}
	}
}

func parse(data string) [][]rune {
	grid := [][]rune{}
	for _, line := range strings.Split(data, "\n") {
		grid = append(grid, []rune(line))
	}
	return grid
}

