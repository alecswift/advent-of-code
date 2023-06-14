package main

import (
	"fmt"
	"strings"

	"github.com/alecswift/advent_of_code/util"
)

func main() {
	grid := parse("/home/alec/Desktop/code/advent-of-code/2017/day_22/input.txt")
	infectedCount := part1(grid)

	grid = parse("/home/alec/Desktop/code/advent-of-code/2017/day_22/input.txt")
	infectedCount2 := part2(grid)

	fmt.Print(infectedCount, "\n", infectedCount2)
}

func part1(grid map[complex128]int) int {
	currPos := complex(12, -12)
	dir := 0
	dirs := []complex128{complex(0,1), complex(1,0), complex(0,-1), complex(-1, 0)}
	infectedCount := 0

	for i := 0; i < 10000; i++ {
		if grid[currPos] == 2 {
			dir = mod((dir + 1), 4)
			grid[currPos] = 0
		} else {
			dir = mod((dir - 1), 4)
			grid[currPos] = 2
			infectedCount += 1
		}
		currPos += dirs[dir]
		_, exists := grid[currPos]
		if !exists {
			grid[currPos] = 0
		}
	}
	return infectedCount
}

func part2(grid map[complex128]int) int {
	currPos := complex(12, -12)
	dir := 0
	dirs := []complex128{complex(0,1), complex(1,0), complex(0,-1), complex(-1, 0)}
	infectedCount := 0

	for i := 0; i < 10000000; i++ {
		switch grid[currPos] {
		case 0:
			dir = mod((dir - 1), 4)
		case 1:
			infectedCount += 1
		case 2:
			dir = mod((dir + 1), 4)
		case 3:
			dir = mod((dir + 2), 4)
		}

		grid[currPos] = mod(grid[currPos] + 1, 4)

		currPos += dirs[dir]
		_, exists := grid[currPos]
		if !exists {
			grid[currPos] = 0
		}
	}
	return infectedCount
}

func mod(a, b int) int {
    return (a % b + b) % b
}

func parse(inputFile string) map[complex128]int {
	data := util.FileToStr(inputFile)
	splitLines := strings.Split(data, "\n")
	grid := make(map[complex128]int)

	for y_coord, row := range splitLines {
		for x_coord, char := range row {
			pos := complex(float64(x_coord), float64(-y_coord))
			isOn := 2
			if char == '.' {isOn = 0}
			grid[pos] = isOn
		}
	}

	return grid
}