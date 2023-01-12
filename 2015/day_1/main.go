// Puzzle explanation: https://adventofcode.com/2022/day/1

package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	inputData := parse("2015/day_1/input.txt")
	solutions := traverseFloors(inputData)
	fmt.Println(solutions[0])
	fmt.Println(solutions[1])
}

func parse(input_file string) string {
	data, err := os.ReadFile(input_file)
	if err != nil {
		log.Fatal(err)
	}
	inputData := string(data)
	return inputData
}

func traverseFloors(inputData string) []int {
	currentFloor := 0
	firstEntry := true
	var basementIdx int
	for idx, direction := range inputData {
		if currentFloor == -1 && firstEntry {
			basementIdx = idx
			firstEntry = false
		}
		if direction == '(' {
			currentFloor += 1
		} else {
			currentFloor -= 1
		}
	}
	return []int{currentFloor, basementIdx} 
}
