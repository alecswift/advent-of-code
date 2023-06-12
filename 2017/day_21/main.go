// Puzzle explanation: https://adventofcode.com/2017/day/21

package main

import (
	"fmt"
	"math"
	"regexp"

	"github.com/alecswift/advent_of_code/util"
)

func main() {
	rules4, rules9 := parse("/home/alec/Desktop/code/advent-of-code/2017/day_21/input.txt")
	fmt.Print(rules4, "\n", len(rules4))
	fmt.Print("\n", rules9, "\n", len(rules9))
}

func parse(inputFile string) (map[int]int, map[int]int) {
	rawData := util.FileToStr(inputFile)
	re := regexp.MustCompile(`[.#/]+`)
	data := re.FindAllString(rawData, -1)
	rules4 := make(map[int]int)
	rules9 := make(map[int]int)

	for i := 0; i < len(data); i += 2 {
		match, conversion := strToBits(data[i]), strToBits(data[i + 1])
		if len(data[i]) == 5 {
			rules4[match] = conversion
		} else {
			rules9[match] = conversion
		}
	}

	return rules4, rules9
}

func strToBits(str string) int {
	var out int
	exponent := len(str) - (int(math.Log2(float64(len(str)))))

	for _, char := range str {
		if char == '/' { continue }
		if char == '#' {
			out += int(math.Pow(2, float64(exponent)))
		}
		exponent -= 1
	}

	return out
}