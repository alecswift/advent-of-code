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
	intervalsIP := findIPIntervals(intervals)
	numberOfValidIPS := countValid(intervalsIP)
	lowest := intervalsIP[0][0]
	fmt.Print(lowest, "\n", numberOfValidIPS)
	// fmt.Print(lowest, "\n")
	// fmt.Print(intervals)
}

func countValid(intervalsIP [][]int) int {
	count := 0
	for _, interval := range intervalsIP {
		low, high := interval[0], interval[1]
		count += high - low + 1
	}
	return count
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
			intervals[pos+1] = intervals[pos]
			pos--
		}
		intervals[pos+1] = val
	}
}

func findIPIntervals(intervals [][]int) [][]int {
	intervalsIP := [][]int{}
	lowBound := intervals[0][0]
	highBound := intervals[0][1]

	if lowBound != 0 {
		intervalsIP = append(intervalsIP, []int{0, lowBound - 1})
	}

	for idx := 1; idx < len(intervals); idx++ {
		currLow := intervals[idx][0]
		currHigh := intervals[idx][1]
		if highBound+1 < currLow {
			lowIP := highBound + 1
			highIP := currLow - 1
			intervalsIP = append(intervalsIP, []int{lowIP, highIP})
			lowBound = currLow
			highBound = currHigh
		} else if highBound < currHigh {
			highBound = currHigh
		}
	}

	if highBound != 4294967295 {
		intervalsIP = append(intervalsIP, []int{highBound + 1, 4294967295})
	}

	return intervalsIP
}
