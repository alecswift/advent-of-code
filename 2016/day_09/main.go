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
	_, length := findLength(file)
	//fmt.Print(newSeq, " ")
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
			chars, times := parseMarker(file, &idx)
			for num := 0; num < times; num++ {
				newSeq += string(file[idx + 1: idx + chars + 1])
			}
			idx += chars
		} else {
			newSeq += string(file[idx])
		}
	}
	return newSeq, utf8.RuneCountInString(newSeq)
}


func parseMarker(file string, pidx *int) (int, int) {
	start := *pidx
	for file[*pidx] != ')' {
		*pidx++
	}
	marker := file[start + 1: *pidx]
	nums := strings.Split(marker, `x`)
	chars, err := strconv.Atoi(nums[0])
	if err != nil {
		panic(err)
	}
	times, err := strconv.Atoi(nums[1])
	if err != nil {
		panic(err)
	}
	return chars, times
}
