package main

import (
	"fmt"
	"strings"

	"github.com/alecswift/advent_of_code/util"
)

func main() {
	inputData := util.FileToStr("/home/alec/Desktop/code/advent_of_code/2016/day_20/input.txt")
	intervals := parse(inputData)
	insertionSort(intervals)
	lowest := findLowest(intervals)
	fmt.Print(lowest)
}

func parse(inputData string) [][]int {
	split_lines := strings.Split(inputData, "\n")
	intervals := [][]int{}
	var low int
	var high int

	for _, line := range split_lines {
		fmt.Sscanf(line, "%d-%d", &low, &high)
		intervals = append(intervals, []int{low, high})
	}

	return intervals
}

func insertionSort(intervals [][]int) {
	for idx := 1; idx < len(intervals); idx++ {
		val := intervals[idx]
		low := val[0]
		pos := idx - 1
		for 0 <= pos && low < intervals[pos][0] {
			intervals[pos + 1] = intervals[pos]
			pos--
		}
		intervals[pos + 1] = val
	}
}

func findLowest(intervals [][]int) int {
	lowBound := intervals[0][0]
	highBound := intervals[0][1]
	if lowBound != 0 {
		return intervals[0][0] - 1
	}
	// add found bool for lowest to use this loop if possible for part 2
	for idx := 1; idx < len(intervals); idx++ {
		currLow := intervals[idx][0]
		currHigh := intervals[idx][1]
		if highBound + 1 < currLow {
			return highBound + 1
		} else if highBound < currHigh {
			highBound = currHigh
		}
	}
	return -1
}
