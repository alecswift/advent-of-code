package main

import (
	"strings"

	"github.com/alecswift/advent_of_code/util"
)

func main() {
	const InitialState = "A"
	const Steps = 12667664
	blueprint := map[string][2][3]int{
		"A": {{1, 1, 66}, {0, -1, 67}},
		"B": {{1, -1, 65}, {1, 1, 68}},
		"C": {{0, -1, 66}, {0, -1, 69}},
		"D": {{1, 1, 65}, {0, 1, 66}},
		"E": {{1, -1, 70}, {1, -1, 67}},
		"F": {{1, 1, 68}, {1, 1, 65}},
	}
}

func parse(inputFile string) map[string][2][3]int {
	data := util.FileToStr(inputFile)
	
	blueprint := make(map[string][2][3]int)

	return blueprint
}