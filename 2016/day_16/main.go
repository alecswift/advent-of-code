// Puzzle explanation: https://adventofcode.com/2016/day/16

package main

import (
	"fmt"
	"strings"
	"unicode/utf8"
)

func main() {
	binString := "11011110011011101"
	revFlip := "01000100110000100"
	diskLength := 272
	new := lSystem(diskLength, binString, revFlip)
	pairs := convertToPairs(new, diskLength)
	solution := findCheckSum(pairs)
	fmt.Print(strings.Join(solution, ""), "\n")

	diskLength = 35651584
	new2 := lSystem(diskLength, binString, revFlip)
	pairs2 := convertToPairs(new2, diskLength)
	solution2 := findCheckSum(pairs2)
	fmt.Print(strings.Join(solution2, ""))
}

func lSystem(DiskLength int, axiom, revFlip string) []string {
	length := utf8.RuneCountInString((axiom))
	var1 := "a"
	var2 := "b"
	const1 := "0"
	const2 := "1"
	var1Conv := []string{var1, const1, var2}
	var2Conv := []string{var1, const2, var2}
	rules := map[string][]string{var1: var1Conv, var2: var2Conv}
	varToStr := map[string]string{var1: axiom, var2: revFlip}
	randomData := []string{"a"}
	for length < DiskLength {
		new := []string{}
		for _, char := range randomData {
			out, exists := rules[string(char)]
			if exists {
				new = append(new, out...)
			} else {
				new = append(new, string(char))
			}
		}
		randomData = new
		length *= 2
		length++
	}
	output := []string{}
	for _, char := range randomData {
		out, exists := varToStr[string(char)]
			if exists {
				output = append(output, out)
			} else {
				output = append(output, string(char))
			}
	}
	return output
}

func findCheckSum(pairs []string) []string {
	for len(pairs) % 2 == 0 {
		new := []string{}
		for idx := 2; idx <= len(pairs); idx += 2 {
			pair := pairs[idx - 2: idx]
			var conversion string
			if areEqual([]string{"1", "1"}, pair) || areEqual([]string{"0", "0"}, pair) {
				conversion = "1"
			} else {
				conversion = "0"
			}
			new = append(new, conversion)
		}
		pairs = new
	}
	return pairs
}

func convertToPairs(randomData []string, DiskLength int) []string {
	joined := strings.Join(randomData, "")
	output := []string{}
	for idx := 0; idx < DiskLength; idx++ {
		output = append(output, string(joined[idx]))
	}
	return output
}

func areEqual(slice1 []string, slice2 []string) bool {
	for idx, char := range slice1 {
		if slice2[idx] != char {
			return false
		}
	}
	return true
}