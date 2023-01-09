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
	idx := 0
	currentFloor := 0
	firstEntry := true
	var basementIdx int
	for idx < len(inputData) {
		if currentFloor == -1 && firstEntry {
			basementIdx = idx
			firstEntry = false
		}
		if string(inputData[idx]) == "(" {
			currentFloor += 1
		} else {
			currentFloor -= 1
		}
		idx += 1
	}
	return []int{currentFloor, basementIdx} 
}
