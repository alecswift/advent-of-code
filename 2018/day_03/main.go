// Puzzle explanation: https://adventofcode.com/2018/day/3

package main

import (
	"fmt"
	"regexp"
	"strings"

	"github.com/alecswift/advent_of_code/stringOps"
	"github.com/alecswift/advent_of_code/util"
)

type Rect struct{
	left   int
	top    int
	width  int
	height int
}
const Dim = 1000
func main() {
	rects := parse("/home/alec/Desktop/code/advent-of-code/2018/day_03/input.txt")
	grid := fillGrid(rects)
	part1 := countOver2(grid)
	part2 := part2(grid, rects)
	fmt.Print(part1, "\n", part2)
}

func part2(grid [Dim][Dim]int, rects []Rect) int {
	for idx, rect := range rects {
		if noOverlap(rect, grid) {
			return idx + 1
		}
	}
	return -1
}

func noOverlap(rect Rect, grid [Dim][Dim]int) bool {
	for i := rect.top; i < rect.top + rect.height; i++ {
		for j := rect.left; j < rect.left + rect.width; j++ {
			if grid[i][j] >= 2 {
				return false
			}
		}
	}
	return true
}

func countOver2(grid [Dim][Dim]int) int {
	var count int

	for _, row := range grid {
		for _, num := range row {
			if num >= 2 {
				count++
			}
		}
	}

	return count
}

func fillGrid(rects []Rect) [Dim][Dim]int {
	grid := [Dim][Dim]int{}

	for _, rect := range rects {
		for i := rect.top; i < rect.top + rect.height; i++ {
			for j := rect.left; j < rect.left + rect.width; j++ {
				grid[i][j]++
			}
		}
	}

	return grid
}

func parse(inputFile string) []Rect {
	data := util.FileToStr(inputFile)
	splitLines := strings.Split(data, "\n")
	out := []Rect{}
	re := regexp.MustCompile(`\d+`)

	for _, line := range splitLines {
		nums := re.FindAllString(line, -1)
		rect := Rect{
			left: stringOps.StrToInt(nums[1]),
			top: stringOps.StrToInt(nums[2]),
			width: stringOps.StrToInt(nums[3]),
			height: stringOps.StrToInt(nums[4]),
		}
		out = append(out, rect)
	}

	return out
}
