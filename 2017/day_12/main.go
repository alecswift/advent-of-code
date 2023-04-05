// Puzzle explanation: https://adventofcode.com/2017/day/12

package main

import (
	"fmt"
	"regexp"
	"strings"

	"github.com/alecswift/advent_of_code/util"
)

func main() {
	adjMap := parse("/home/alec/Desktop/code/advent-of-code/2017/day_12/input.txt")
	ttlPros := 0
	pTtlPros := &ttlPros
	seen := make(map[string]bool)
	dfs(adjMap, pTtlPros, "0", seen)

	groups := 0
	pGroups := &groups
	part2(adjMap, pGroups)

	fmt.Print(*pTtlPros, "\n", *pGroups)
}

func part2(adjMap map[string][]string, pGroups *int) {
	seen := make(map[string]bool)
	ttlPros := 0
	pTtlPros := &ttlPros


	for node := range adjMap {
		_, visited := seen[node]

		if !visited {
			*pGroups++
			dfs(adjMap, pTtlPros, node, seen)
		}
	}
}

func dfs(adjMap map[string][]string, pTtlPros *int, node string, seen map[string]bool) {
	seen[node] = true
	*pTtlPros++

	for _, neighbor := range adjMap[node] {
		_, visited := seen[neighbor]

		if !visited {
			dfs(adjMap, pTtlPros, neighbor, seen)
		}
	}
}

func parse(inputFile string) map[string][]string {
	inputData := util.FileToStr(inputFile)
	splitLines := strings.Split(inputData, "\n")
	adjMap := make(map[string][]string)

	for _, line := range splitLines {
		re := regexp.MustCompile(`\d+`)
		data := re.FindAllString(line, -1)
		program := data[0]
		neighbors := data[1:]

		adjMap[program] = neighbors
	}

	return adjMap
}
