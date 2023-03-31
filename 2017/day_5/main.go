// Puzzle explanation: https://adventofcode.com/2017/day/5

package main

import (
	"fmt"
	"strings"

	"github.com/alecswift/advent_of_code/arrayOps"
	"github.com/alecswift/advent_of_code/util"
)

func main() {
	nums := parse("/home/alec/Desktop/code/advent_of_code/2017/day_5/input.txt")
	steps1 := traverse(nums, true)
	nums = parse("/home/alec/Desktop/code/advent_of_code/2017/day_5/input.txt")
	steps2 := traverse(nums, false)
	fmt.Print(steps1, "\n", steps2)
}

func traverse(nums []int, part1 bool) int {
	var prevIdx int
	steps := 0
	idx := 0

	for idx > -1 && idx < len(nums) {

		if part1 {
			prevIdx = idx
			idx += nums[idx]
			nums[prevIdx]++
		} else {
			prevIdx = idx
			idx += nums[idx]
			if nums[prevIdx] >= 3 {
				nums[prevIdx]--
			} else {
				nums[prevIdx]++
			}
		}

		steps++
	}

	return steps
}

func parse(file_name string) []int {
	data := util.FileToStr(file_name)
	splitLines := strings.Split(data, "\n")
	nums := arrayOps.StrListToIntList(splitLines)

	return nums
}
