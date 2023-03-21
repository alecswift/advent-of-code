// Puzzle explanation: https://adventofcode.com/2016/day/17

package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"io"
	"unicode/utf8"
)
func main() {
	passCode := "ioramepc"
	puzzleMap := []string{
		"#########",
        "#S| | | #",
        "#-#-#-#-#",
        "# | | | #",
        "#-#-#-#-#",
        "# | | | #",
        "#-#-#-#-#",
        "# | | |V",
        "#######  ",
	}
	shortestpath, longest_length := bfs(puzzleMap, passCode)
	fmt.Print(shortestpath, "\n")
	fmt.Print(longest_length)
}

func bfs(puzzleMap []string, passCode string) (string, int) {
	var part1 string
	var part2 int
	start := []int{1, 1}
	queuePos := [][]int{start}
	queuePath := []string{""}
	directions := map[string][]int{
		"U": {-1, 0, 0},
		"D": {1, 0, 1},
		"L": {0, -1, 2},
		"R": {0, 1, 3},
	}
	valid := map[rune]int{'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}
	for len(queuePos) != 0 {
		row, col := queuePos[0][0], queuePos[0][1]
		curr_path := queuePath[0]
		for direction, data := range directions {
			rowChg, colChg := data[0], data[1]
			next_row, next_col := row + rowChg, col + colChg
			if puzzleMap[next_row][next_col] == '#' {
				continue;
			}

			idx := data[2]
			hash := makeHash(passCode, curr_path)
			_, doorOpen := valid[rune(hash[idx])]
			if !doorOpen {
				continue;
			}

			if next_row + rowChg == 7 && next_col + colChg == 7 {
				if part1 == "" {
					part1 = curr_path + direction
				}
				part2 = utf8.RuneCountInString(curr_path + direction)
				continue;
			}

			queuePos = append(queuePos, []int{next_row + rowChg, next_col + colChg})
			queuePath = append(queuePath, curr_path + direction)
		}
		queuePos = queuePos[1:]
		queuePath = queuePath[1:]
	}
	return part1, part2
}

func makeHash(key, path string) string {
	hash := md5.New()
	io.WriteString(hash, key)
	io.WriteString(hash, path)
	return hex.EncodeToString(hash.Sum(nil))
}