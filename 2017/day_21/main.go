// Puzzle explanation: https://adventofcode.com/2017/day/21

package main

import (
	"fmt"
	"math"
	"regexp"

	"github.com/alecswift/advent_of_code/util"
)

func main() {
	rules := parse("/home/alec/Desktop/code/advent-of-code/2017/day_21/input.txt")
	fmt.Print(rules)
}

func parse(inputFile string) map[int]int {
	rawData := util.FileToStr(inputFile)
	re := regexp.MustCompile(`[.#/]+`)
	data := re.FindAllString(rawData, -1)
	rules := make(map[int]int)

	for i := 1; i < len(data); i += 2 {
		match, conversion := strToBits(data[i - 1]), strToBits(data[i])
		rules[match] = conversion
	}

	return rules
}

func strToBits(str string) int {
	var out int
	exponent := len(str) - (int(math.Log2(float64(len(str)))) - 1)

	for _, char := range str {
		if char == '/' { continue }
		if char == '#' {
			out += 2 ^ exponent
		}
		exponent -= 1
	}

	return out
}