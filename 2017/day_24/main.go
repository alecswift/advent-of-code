package main

import (
	"fmt"
	"strings"

	"github.com/alecswift/advent_of_code/stringOps"
	"github.com/alecswift/advent_of_code/util"
)

func main() {
	ports := parse("/home/alec/Desktop/code/advent-of-code/2017/day_24/input.txt")
	maxPaths := dfs(ports, make(map[[2]int]bool), 0, 0, []int{})
	fmt.Print(max(maxPaths))
}

func dfs(ports map[int][][2]int, cache map[[2]int]bool, currNode, maxPath int, maxPaths []int) []int {

	for _, neighbor := range ports[currNode] {
		_, visited := cache[neighbor]
		if visited {continue}

		var nextNode int
		if neighbor[0] == currNode {
			nextNode = neighbor[1]
		} else {
			nextNode = neighbor[0]
		}

		cache[neighbor] = true
		maxPaths = dfs(ports, cache, nextNode, maxPath + nextNode, maxPaths)
	}
	maxPaths = append(maxPaths, maxPath)
	return maxPaths
}

func max(nums []int) int {
	var max int
	for idx, num := range nums {
		if idx == 0 || max < num {
			max = num
		}
	}
	return max
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

		for _, num := range port {
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