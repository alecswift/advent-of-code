// Puzzle explanation: https://adventofcode.com/2017/day/3

package main

import (
	"fmt"
	"math"
)

func main() {
	input := 265149
	part_1 := part_1_sol(float64(input))
	part_2 := part_2_sol(input)
	fmt.Print(part_1, "\n", part_2)
}

func part_1_sol(num float64) int {
	cornerRoot := math.Ceil(math.Pow(num, 0.5))

	if int(cornerRoot) % 2 == 0 {
		cornerRoot += 1
	}

	cornerVal := math.Pow(cornerRoot, 2)
	diff := cornerVal - num
	numOfDistances := int((cornerRoot + 1) / 2)
	distance := int((cornerRoot - 1)) - (int(diff) % numOfDistances)
	
	return distance
}

func part_2_sol(num int) int {
	row := [11]int{}
	matrix := [11][11]int{row}
	matrix[5][5] = 1
	// right, up, left, down
	directions := [][2]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}}
	neighbors := [][2]int{{1, 1}, {-1, 1}, {1, -1}, {-1, -1}}
	neighbors = append(neighbors, directions...)
	pos := [2]int{6, 5}
	idx := 0
	var val int

	for val < num {
		row, col := pos[0], pos[1]
		val = 0

		for _, neighbor := range neighbors {
			newRow, newCol := row + neighbor[0], col + neighbor[1]
			val += matrix[newRow][newCol]
		}
		matrix[row][col] = val

		tempIdx := (idx + 1) % 4
		tempDir := directions[tempIdx]
		tempRow, tempCol := row + tempDir[0], col + tempDir[1]

		if matrix[tempRow][tempCol] == 0 {
			idx = tempIdx
			pos = [2]int{tempRow, tempCol}
		} else {
			pos = [2]int{row + directions[idx][0], col + directions[idx][1]}
		}
	}
	
	return val
}

