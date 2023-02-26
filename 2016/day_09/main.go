// Puzzle explanation: https://adventofcode.com/2016/day/9

package main

import (
	"fmt"
	"os"
	"unicode/utf8"
	"strconv"
	"strings"
)

func main() {
	file := parse("2016/day_09/input.txt")
	newSeq, length := findLength(file)
	fmt.Print(newSeq, " ")
	fmt.Print(length)
}

func parse(inputFile string) string {
	inputData, err := os.ReadFile(inputFile)
	if err != nil {
		panic(err)
	}
	file := string(inputData)
	return file
}

func findLength(file string) (string, int) {
	newSeq := ""
	for idx := 0; idx < utf8.RuneCountInString(file); idx++ {
		if file[idx] == '(' {
			idx2 := idx
			for file[idx2] != ')' {
				idx2++
			}
			marker := file[idx + 1: idx2]
			nums := strings.Split(marker, `x`)

			times, err := strconv.Atoi(nums[1])
			if err != nil {
				panic(err)
			}
			chars, err := strconv.Atoi(nums[0])
			if err != nil {
				panic(err)
			}
			for num := 0; num < times; num++ {
				newSeq += string(file[idx2 + 1: idx2 + chars + 1])
			}
			idx = idx2 + chars
		} else {
			newSeq += string(file[idx])
		}
	}
	return newSeq, utf8.RuneCountInString(newSeq)
}
