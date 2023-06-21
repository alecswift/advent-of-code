package main

import (
	"fmt"
	"strings"

	"github.com/alecswift/advent_of_code/stringOps"
	. "github.com/alecswift/advent_of_code/util"
)

type Coord struct{
	row  int
	col  int
	area int
}

func main() {
	coords := parse("/home/alec/Desktop/code/advent-of-code/2018/day_06/input.txt")
	grid := setGrid(coords)
	maxArea := findAreas(coords, grid)
	areaLess10000 := areaPart2(coords)
	fmt.Print(maxArea, "\n", areaLess10000)
}

func areaPart2(coords []Coord) int {
	count := 0

	for i := -350; i < 350; i++ {
		for j := -350; j < 350; j++ {
			totalDist := totalDist(coords, i, j)
			if totalDist < 10000 {count++}
		}
	}

	return count
}

func totalDist(coords []Coord, row, col int) int {
	total := 0

	for _, coord := range coords {
		total += ManhattanDistance(row, col, coord.row, coord.col)
	}

	return total
}

func findAreas(coords []Coord, grid [][]int) int {
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			isBorder := i == 0 || j == 0 || i == len(grid) - 1 || j == len(grid[0]) - 1
			coordIdx := grid[i][j]

			if coordIdx == -1 {continue}
			if isBorder {coords[coordIdx].area = -1}
			if coords[coordIdx].area == -1 {continue}
			coords[coordIdx].area++
		}
	}

	var maxArea int

	for idx, coord := range coords {
		if coord.area != -1 && (idx == 0 || maxArea < coord.area) {
			maxArea = coord.area
		}
	}

	return maxArea
}

func setGrid(coords []Coord) [][]int {
	maxRow, maxCol := findBorders(coords)
	grid := [][]int{}

	for i := 0; i <= maxRow; i++ {
		grid = append(grid, []int{})
		for j := 0; j <= maxCol; j++ {
			minIdx := minDist(coords, i, j)
			grid[i] = append(grid[i], minIdx)
		}
	}

	return grid
}

func minDist(coords []Coord, row, col int) int {
	var minIdx, minVal []int

	for idx, coord := range coords {
		dist := ManhattanDistance(coord.row, coord.col, row, col)
		
		if idx == 0 || dist < minVal[0] {
			minIdx = []int{idx}
			minVal = []int{dist}
		} else if dist == minVal[0] {
			minIdx = append(minIdx, idx)
			minVal = append(minVal, dist)
		}
	}
	
	if len(minIdx) > 1 {
		return -1
	} else {
		return minIdx[0]
	}
}

func findBorders(coords []Coord) (int, int) {
	var maxRow, maxCol int

	for idx, coord := range coords {
		if idx == 0 || coord.row > maxRow {
			maxRow = coord.row
		}
		if idx == 0 || coord.col > maxCol {
			maxCol = coord.col
		}
	}
	
	return maxRow, maxCol
}

func parse(inputFile string) []Coord {
	data := FileToStr(inputFile)
	splitLines := strings.Split(data, "\n")
	coords := []Coord{}

	for _, line := range splitLines {
		raw := strings.Split(line, ", ")
		coord := Coord{
			row: stringOps.StrToInt(raw[1]),
			col: stringOps.StrToInt(raw[0]),
		}
		coords = append(coords, coord)
	}

	return coords
}
