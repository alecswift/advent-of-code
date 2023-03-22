// Puzzle explanation: https://adventofcode.com/2016/day/18

package main

import (
	"fmt"
	"strings"
	"unicode/utf8"
	"github.com/alecswift/advent_of_code/util"
)
func main() {
	startStr := util.FileToStr("/home/alec/Desktop/code/advent_of_code/2016/day_18/input.txt")
	rows := 40
	cols := utf8.RuneCountInString(startStr)
	grid := buildGrid(startStr, rows, cols)
	determineTiles(grid, rows, cols)
	part1 := countSafe(grid)
	fmt.Print(part1, "\n")

	rows2 := 400000
	grid2 := buildGrid(startStr, rows2, cols)
	determineTiles(grid2, rows2, cols)
	part2 := countSafe(grid2)
	fmt.Print(part2)
}

func buildGrid(startStr string, rows, cols int) [][]string{
	startRow := strings.Split(startStr, "")
	grid := make([][]string, rows)
	grid[0] = startRow
	for rowNum := 1; rowNum < rows; rowNum++ {
		row := make([]string, cols)
		for colNum := 0; colNum < cols; colNum++ {
			row[colNum] = "."
		}
		grid[rowNum] = row
	}
	return grid
}

func determineTiles(grid [][]string, rows, cols int) {
	left := []int{-1, -1}
	center := []int{-1, 0}
	right := []int{-1, 1}
	for row_num := 1; row_num < rows; row_num++ {
		for col_num := 0; col_num < cols; col_num++ {
			var leftVal string
			var rightVal string
			if col_num + left[1] == -1 {
				leftVal = "."
			} else {
				leftVal = grid[row_num + left[0]][col_num + left[1]]
			}
			if col_num + right[1] == cols {
				rightVal = "."
			} else {
				rightVal = grid[row_num + right[0]][col_num + right[1]]
			}
			centerVal := grid[row_num + center[0]][col_num + center[1]]
			allSame := leftVal == centerVal && centerVal == rightVal
			leftRightTrap := centerVal == "." && centerVal != leftVal && centerVal != rightVal
			centerTrap := centerVal == "^" && centerVal != leftVal && centerVal != rightVal
			isSafe := allSame || leftRightTrap || centerTrap
			
			if isSafe {
				grid[row_num][col_num] = "."
			} else {
				grid[row_num][col_num] = "^"
			}
		}
	}
}

func countSafe(grid [][]string) int {
	var count int
	for _, row := range grid {
		for _, val := range row {
			if val == "." {
				count += 1
			}
		}
	}
	return count
}
