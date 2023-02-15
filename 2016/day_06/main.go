// Puzzle explanation: https://adventofcode.com/2016/day/6

package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	rows := parse("/home/alec/Desktop/code/advent_of_code/2016/day_06/input.txt")
	charCounts := findCharCounts(rows)
	word1 := findWord(charCounts, true)
	word2 := findWord(charCounts, false)
	fmt.Print(word1)
	fmt.Print("\n", word2)
}

func parse(inputFile string) []string {
	inFile, err := os.ReadFile(inputFile)
	if err != nil {
		panic(err)
	}
	rows := strings.Split(string(inFile), "\n")
	return rows
}

func findCharCounts(rows []string) []map[rune]int {
	charCounts := []map[rune]int{}
	for i := 0; i < 8; i++ {
		charCount := map[rune]int{}
		charCounts = append(charCounts, charCount)
	}

	for _, row := range rows {
		for idx, char := range row {
			_, charInCounts := charCounts[idx][char]
			if charInCounts {
				charCounts[idx][char] += 1
			} else {
				charCounts[idx][char] = 1
			}
		}
	}
	return charCounts
}

func findWord(charCounts []map[rune]int, part1 bool) string {
	type FindChar struct {
		char  rune
		count int
	}
	word := ""
	for _, charCount := range charCounts {
		findChar := FindChar {
			char: ' ',
			count: 0,
		}
		for char, count := range charCount {
			if findChar.count == 0 {
				findChar.char = char
				findChar.count = count
			} else if part1 && findChar.count < count {
				findChar.char = char
				findChar.count = count
			} else if !part1 && count < findChar.count {
				findChar.char = char
				findChar.count = count
			}
		}
		word += string(findChar.char)
	}
	return word
}
