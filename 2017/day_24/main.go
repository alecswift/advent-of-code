package main

import (
	"fmt"
	"reflect"
	"strings"

	"github.com/alecswift/advent_of_code/stringOps"
	"github.com/alecswift/advent_of_code/util"
)

func main() {
	ports := parse("/home/alec/Desktop/code/advent-of-code/2017/day_24/input.txt")
	maxPaths := dfs(ports, 0, [][2]int{}, [][][2]int{})
	copy := [][2]int{{0,35},{22,35},{0,22},{0,7},{28,7},{28,28},{19,28},{19,27},{27,39},{39,14},{3,14},{3,31},{20,31},{20,47},{47,15},{15,33},{1,33},{1,10},{10,40},{40,20},{15,20},{46,15},{46,44},{30,44},{30,30},{30,43},{43,43},{43,45},{45,45},{45,8},{8,42},{50,42},{34,50},{34,32}, {34,32}}
	for _, path := range maxPaths {
	    if reflect.DeepEqual(path, copy) {
		    fmt.Print("hello")
	    }
	}
	fmt.Print(findMaxWeight(maxPaths))
	maxLengths := buildMaxLengths(maxPaths)
	ayo := findMaxWeight(maxLengths)
	fmt.Print("\n", ayo)
}

func dfs(ports map[int][][2]int, currNode int, maxPath [][2]int, maxPaths [][][2]int) [][][2]int {

	for _, neighbor := range ports[currNode] {
		visited := false
		for _, node := range maxPath {
			if node == neighbor {
				visited = true
			}
		}
		if visited {
			continue
		}

		var nextNode int
		if neighbor[0] == currNode {
			nextNode = neighbor[1]
		} else {
			nextNode = neighbor[0]
		}
		temp := make([][2]int, len(maxPath))
		copy(temp, maxPath)	
		maxPath = temp
		maxPaths = dfs(ports, nextNode, append(maxPath, neighbor), maxPaths)
	}
	maxPaths = append(maxPaths, maxPath)
	return maxPaths
}

func findMaxWeight(paths [][][2]int) int {
	var maxWeight int

	for idx, path := range paths {
		weight := 0

		for _, node := range path {
			weight += node[0] + node[1]
		}
		if idx == 0 || maxWeight < weight {
			maxWeight = weight
		}
	}
	return maxWeight
}

func buildMaxLengths(paths [][][2]int) [][][2]int {
	var maxLength int
	var maxLengths [][][2]int

	for idx, path := range paths {
		if idx == 0 || maxLength < len(path) {
			maxLength = len(path)
			maxLengths = [][][2]int{path}
		} else if maxLength == len(path) {
			maxLengths = append(maxLengths, path)
		}
	}
	return maxLengths
}

func parse(inputFile string) map[int][][2]int {
	data := util.FileToStr(inputFile)
	splitLines := strings.Split(data, "\n")
	ports :=  map[int][][2]int{}

	for _, line := range splitLines {
		split := strings.Split(line, "/")
		port := [2]int{}
		for idx, strNum := range split {
			port[idx] = stringOps.StrToInt(strNum)
		}
		for idx, num := range port {
			if port[0] == port[1] && idx == 1 {break}
			addToDict(num, port, ports)
		}
	}
	return ports
}

func addToDict(key int, val [2]int, dict map[int][][2]int) {
	_, exists := dict[key]

	if !exists {
		dict[key] = [][2]int{val}
	} else {
		dict[key] = append(dict[key], val)
	}
}