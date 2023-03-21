// Puzzle explanation: https://adventofcode.com/2016/day/15

package main

import (
	"fmt"
	"os"
	"regexp"
)
func main() {
	discs := parse("/home/alec/Desktop/code/advent_of_code/2016/day_15/input.txt")
	time := dropCapsules(discs)
	discs = parse("/home/alec/Desktop/code/advent_of_code/2016/day_15/input.txt")
	discs = append(discs, []int{11, 0})
	timePartTwo := dropCapsules(discs)
	fmt.Print(time, "\n")
	print(timePartTwo)
}

func parse(inputFile string) [][]int {
	inputData, err := os.ReadFile(inputFile)
	if err != nil {
		panic(err)
	}
	splitLines := regexp.MustCompile(`\n`).Split(string(inputData), -1)
	discs := [][]int{}
	for _, line := range splitLines {
		var x int
		var y int
		var z int
		fmt.Sscanf(line, "Disc #%d has %d positions; at time=0, it is at position %d.", &x, &y, &z)
		discs = append(discs, []int{y,z})
	}
	return discs
}

func dropCapsules(discs [][]int) int {
	numCapsules := len(discs)
	capsule0 := []int{0,0,1}
	// popped, start time, curr position
	capsules := [][]int{capsule0}
	time := 1
	moveDiscs(discs)
	for true {
		time++
		moveDiscs(discs)

		for _, capsule := range capsules {
			popped, startTime, curr_time := capsule[0], capsule[1], capsule[2]
			if popped == 1 {
				continue;
			}
			diskPos := discs[curr_time][1]
			if diskPos == 0 {
				capsule[2]++
			} else {
				capsule[0] = 1
			}
			if capsule[2] == numCapsules {
				return startTime
			}
		}

		if len(capsules) == numCapsules {
			capsules = capsules[1:numCapsules]
		}
		capsules = append(capsules, []int{0, time, 0})
	}
	return -1
}

func moveDiscs(discs [][]int) {
	for _, disc := range discs {
		max_pos, pos := disc[0], disc[1] 
		if pos == (max_pos - 1) {
			disc[1] = 0
		} else {
			disc[1]++
		}
	}
}