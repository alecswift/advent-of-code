// Puzzle explanation: https://adventofcode.com/2017/day/14

package main

import (
	"fmt"
	"encoding/hex"
	"strconv"

	"github.com/alecswift/advent_of_code/2017/hashList"
)

func main() {
	input := "wenycdww"
	byteInput := []byte(input)
	byteInput = append(byteInput, '-')

	grid := makeGrid(byteInput)
	part1Sol := len(grid)
	part2Sol := part2(grid)
	fmt.Print(part1Sol, "\n", part2Sol)
}

func part2(grid map[[2]int]bool) int {
	var countGroups int
	moves := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	for pos, unvisited := range grid {
		if unvisited {
			grid[pos] = false
			countGroups++
			dfs(pos, grid, moves)
		}
	}

	return countGroups
}

func dfs(pos [2]int, grid map[[2]int]bool, moves [][2]int) {
	for _, move := range(moves) {
		neighbor := [2]int{move[0] + pos[0], move[1] + pos[1]}
		unvisited, exists := grid[neighbor]

		if exists && unvisited{
			grid[neighbor] = false
			dfs(neighbor, grid, moves)
		}
	}
}

func makeGrid(byteLengths []byte) map[[2]int]bool {
	grid := make(map[[2]int]bool)

	for i := 0; i < 128; i++ {
		nums := genNums()
		hash := makeHash(byteLengths, nums, i)
		bytes, err := hex.DecodeString(hash)
		if err != nil {
			panic(err)
		}

		idx := 0
		for _, byte_ := range bytes {
			for bit_idx := 7; bit_idx >= 0; bit_idx-- {
				bit := byte(1 << bit_idx)

				if byte_ & bit != 0 {
					grid[[2]int{i, idx}] = true
				}
	
				idx++
			}
		}
	}

	return grid
}

func countSet(byte_ byte) int {
	count := 0

	for byte_ != 0 {
		count += int(byte_ & 1)
		byte_ >>= 1
	}

	return count
}

func makeHash(byteLengths []byte, nums []int, num int) string {
	numStr := strconv.Itoa(num)
	byteLengths = append(byteLengths, []byte(numStr)...)
	extraBytes := []byte{17, 31, 73, 47, 23}
	byteLengths = append(byteLengths, extraBytes...)

	hexString := hashList.Part2Hash(nums, byteLengths)
	return hexString
}

func genNums() []int {
	nums := make([]int, 256)

	for i := 0; i < 256; i++ {
		nums[i] = i
	}

	return nums
}