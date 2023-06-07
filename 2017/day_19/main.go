package main

import (
	"os"
	"fmt"
	"strings"
	"unicode"
)

func main() {
	pathStr, err := os.ReadFile("/home/alec/Desktop/code/advent-of-code/2017/day_19/input.txt")
	if err != nil {
		panic(err)
	}
	path := strings.Split(string(pathStr), "\n")
	path = addBorders(path)
	start := [2]int{}

	for idx, val := range path[1] {
		if val == '|' {
			start[1] = idx
		}
	}

	start[0] = 1

	sequence := bfs(path, start, [2]int{1, 0})

	fmt.Print(sequence)
}

func addBorders(path []string) []string {
	border := ""
	for i := 0; i < len(path[0]); i++ {
		border += " "
	}
	path = append(path, border)
	for i := 0; i < len(path); i++ {
		path[i] = " " + path[i] + " "
	}
	return path
}

func bfs(path []string, startPos [2]int, startDir [2]int) string {
	sequence := ""
	sequenceAdd := ""
	directions := [][2]int{{0, 1}, {1, 0}, {-1, 0}, {0, -1}}
	currPos := startPos
	currDir := startDir

	for true {
		currPos, sequenceAdd = followLine(path, currPos, currDir)
		sequence += sequenceAdd
		row, col := currPos[0], currPos[1]
		currVal := path[row][col]

		if currVal == ' ' {
			return sequence
		}

		for _, direction := range directions {
			row, col := currPos[0], currPos[1]
			rowChg, colChg := direction[0], direction[1]
			if abs(rowChg) == abs(currDir[0]) && abs(colChg) == abs(currDir[1]) {continue} 

			neighborRow, neighborCol := row + rowChg, col + colChg
			if path[neighborRow][neighborCol] == ' ' {continue}
			
			currPos = [2]int{neighborRow, neighborCol}
			currDir = direction
			break
		}
	}
	return sequence
}

func followLine(path []string, coord, direction [2]int) ([2]int, string) {
	row, col := coord[0], coord[1]
	sequence := ""
	for path[row][col] != ' ' && path[row][col] != '+' {
		char := path[row][col]
		if unicode.IsLetter(rune(char)) {
			sequence += string(char)
		}
		row, col = move(row, col, direction)
	}
	newPos := [2]int{row, col}
	return newPos, sequence
}

func move(row, col int, direction [2]int) (int, int) {
	rowChg, colChg := direction[0], direction[1]
	row += rowChg
	col += colChg
	return row, col
}

func abs(num int) int {
	if num >= 0 {
		return num
	}
	return -num
}