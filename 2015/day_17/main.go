package main

import (
	"fmt"
	"os"
	"strconv"
	"regexp"
)

func main() {
	nums := parse("2015/day_17/input.txt")
	insertionSort(nums)
	fmt.Print(nums)
}

func parse(inputFile string) []int {
	inputData, err := os.ReadFile(inputFile)
	if err != nil {
		panic(err)
	}
	var nums []int
	re := regexp.MustCompile(`\d+`)
	for _, strnum := range re.FindAllString(string(inputData), -1) {
		num, err := strconv.Atoi(strnum)
		if err != nil {
			panic(err)
		}
		nums = append(nums, num)
	}
	return nums
}

func insertionSort(nums []int) {
	for i := 1; i < len(nums); i++ {
		val := nums[i]
		pos := i - 1
		for 0 <= pos && nums[pos] < val {
			nums[pos + 1] = nums[pos]
			pos--
		}
		nums[pos + 1] = val
	}
}

func num_of_combinations(nums []int, target int) int {
	count := 0
	for idx, num := range nums {
		current_sum := num
		for _, adder := range nums[idx+1:] {
			current_sum += adder
			if target < current_sum {
				current_sum -= adder
				continue
			} else if current_sum < target {
				continue
			} else {
				count++
				current_sum -= adder
			}
		}
	}
}