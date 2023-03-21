package main

import (
	"fmt"
	"strings"
	"github.com/alecswift/advent_of_code/util"
)
func main() {
	startStr := util.FileToStr("/home/alec/Desktop/code/advent_of_code/2016/day_18/input.txt")
	grid := buildGrid(startStr)
	fmt.Print(grid)
}

func buildGrid(startStr string) [][]string{
	startRow := strings.Split(startStr, "")
	rows := 40
	cols := len(startRow)
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