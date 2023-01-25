package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func main() {
	prototype := map[string]int{
		"children":    3,
		"cats":        7,
		"samoyeds":    2,
		"pomeranians": 3,
		"akitas":      0,
		"vizslas":     0,
		"goldfish":    5,
		"trees":       3,
		"cars":        2,
		"perfumes":    1,
	}
	sues := parse("2015/day_16/input.txt")
	part1, part2 := findSue(sues, prototype)
	fmt.Printf("%d\n%d", part1, part2)
}

func parse(inputFile string) []map[string]int {
	input_data, err := os.ReadFile(inputFile)
	if err != nil {
		panic(err)
	}
	re := regexp.MustCompile(`\n`)
	splitLines := re.Split(string(input_data), -1)

	var sues []map[string]int
	renums := regexp.MustCompile(`\d+`)
	reitems := regexp.MustCompile(`[a-z]+`)
	for _, line := range splitLines {
		items := reitems.FindAllString(line, -1)
		strnums := renums.FindAllString(line, -1)

		var nums []int
		for _, strnum := range strnums {
			num, err := strconv.Atoi(strnum)
			if err != nil {
				panic(err)
			}
			nums = append(nums, num)
		}

		sues = append(
			sues,
			map[string]int{
				items[1]: nums[1],
				items[2]: nums[2],
				items[3]: nums[3],
			})
	}
	return sues
}

func findSue(sues []map[string]int, prototype map[string]int) (int, int) {
	var part1 int
	var part2 int
	for idx, sue := range sues {
		if part1Check(prototype, sue) {
			part1 = idx + 1
		}
		if part2Check(prototype, sue) {
			part2 = idx + 1
		}
	}
	return part1, part2
}

func part1Check(prototype map[string]int, sue map[string]int) bool {
	match := 0
	for item, num := range sue {
		if prototype[item] == num {
			match++
		}
	}

	if match == 3 {
		return true
	}
	return false
}

func part2Check(prototype map[string]int, sue map[string]int) bool {
	match := 0
	for item, num := range sue {
		if item == "cats" || item == "trees" {
			if prototype[item] < num {
				match++
			}
		} else if item == "pomeranians" || item == "goldfish" {
			if prototype[item] > num {
				match++
			}
		} else if prototype[item] == num {
			match++
		}
	}

	if match == 3 {
		return true
	}
	return false
}
