package main

import (
	"fmt"
	"strings"

	"github.com/alecswift/advent_of_code/util"
)

func main() {
	grid := parse("/home/alec/Desktop/code/advent-of-code/2017/day_22/input.txt")
	
	infectedCount := part1(grid)

	fmt.Print(infectedCount)
}

func part1(grid map[complex128]bool) int {
	currPos := complex(12, -12)
	dir := 0
	dirs := []complex128{complex(0,1), complex(1,0), complex(0,-1), complex(-1, 0)}
	infectedCount := 0

	for i := 0; i < 10000; i++ {
		if grid[currPos] {
			dir = (dir + 1) % 4
			grid[currPos] = false
		} else {
			dir = (dir - 1) % 4
			grid[currPos] = true
			infectedCount += 1
		}
		currPos += dirs[dir]
		_, exists := grid[currPos]
		if !exists {
			grid[currPos] = false
		}
	}
	return infectedCount
}

func parse(inputFile string) map[complex128]bool {
	data := util.FileToStr(inputFile)
	splitLines := strings.Split(data, "\n")
	grid := make(map[complex128]bool)

	for y_coord, row := range splitLines {
		for x_coord, char := range row {
			pos := complex(float64(x_coord), float64(-y_coord))
			isOn := true
			if char == '.' {isOn = false}
			grid[pos] = isOn
		}
	}

	return grid
}