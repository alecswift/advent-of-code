package main

import (
	"fmt"
	"strings"

	"github.com/alecswift/advent_of_code/arrayOps"
	"github.com/alecswift/advent_of_code/util"
)

func main() {
	inputData := util.FileToStr("/home/alec/Desktop/code/advent-of-code/2017/day_10/input.txt")
	lengthsStr := strings.Split(inputData, ",")
	lengths := arrayOps.StrListToIntList(lengthsStr)
	nums := []int{}

	for i := 0; i < 256; i++ {
		nums = append(nums, i)
	}

	hashList(nums, lengths)
	part1 := nums[0] * nums[1]
	fmt.Print(part1)
}

func hashList(nums, lengths []int) {
	pos := 0
	for idx, length := range lengths {
		end := (pos + length) % len(nums)

		arrayOps.ReverseFrom(nums, pos, end)
		pos += length
		pos += idx
		pos %= len(nums)
	}
}