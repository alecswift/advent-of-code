// https://adventofcode.com/2023/day/1

package main

import (
	"fmt"
	"regexp"
	"strings"

	"github.com/alecswift/advent_of_code/stringOps"
	"github.com/alecswift/advent_of_code/util"
)

func main() {
	strData := util.FileToStr("/home/alec/Desktop/code/advent-of-code/2023/input.txt")
	part1Sol := part1(strData)
	part2Sol := part2(strData)
	fmt.Print(part1Sol, "\n", part2Sol)
}

func part1(data string) int {
	lines := strings.Split(data, "\n")
	sum := 0

	for _, line := range lines {
		re := regexp.MustCompile(`\d`)
		digits := re.FindAllString(line, -1)
		firstLast := digits[0] + digits[len(digits) - 1]
		num := stringOps.StrToInt(firstLast)
		sum += num
	}

	return sum
}

func part2(data string) int {
	lines := strings.Split(data, "\n")
	sum := 0

	for _, line := range lines {
		first, last := findDigits(line)
		num := stringOps.StrToInt(first + last)
		sum += num
	}

	return sum
}

func findDigits(line string) (string, string) {
	outDigits := []string{}
	digits := map[string]bool{
		"1": true,
		"2": true,
		"3": true,
		"4": true,
		"5": true,
		"6": true,
		"7": true,
		"8": true,
		"9": true,
	}
	digMap := map[string]string{
		"one": "1",
		"two": "2",
		"three": "3",
		"four": "4",
		"five": "5",
		"six": "6",
		"seven": "7",
		"eight": "8",
		"nine": "9",
	}

	for idx, char := range line {
		exists, _ := digits[string(char)]
		if exists {
			outDigits = append(outDigits, string(char))
		} else {
			for num, dig := range digMap {
				if idx + len(num) <= len(line) && num == line[idx: idx + len(num)] {
					outDigits = append(outDigits, dig)
				}
			}
		}
	}

	return outDigits[0], outDigits[len(outDigits) - 1]
}
