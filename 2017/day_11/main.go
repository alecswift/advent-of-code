//

package main

import (
	"fmt"
	"strings"

	"github.com/alecswift/advent_of_code/util"
)

func main() {
	path := parse("/home/alec/Desktop/code/advent-of-code/2017/day_11/input.txt")
	pos, maxDist := findLocation(path)
	steps := distFromStart(pos)
	fmt.Print(steps, "\n", maxDist)
}

func distFromStart(end [2]float64) float64 {
	/* Derived distance for hexagonal grid from point (0, 0) to an end point */
	x_coord, y_coord := end[0], end[1]
	x_dist := abs(x_coord) / 0.75
	y_dist := abs(y_coord) - (x_dist * 0.5)
	dist := x_dist + y_dist

	return dist
}

func findLocation(path []string) ([2]float64, float64) {
	pos := [2]float64{0, 0}
	dirs := map[string][2]float64{"n": {0, 1}, "s": {0, -1}, "ne": {0.75, 0.5}, "se": {0.75, -0.5}, "nw": {-0.75, .5}, "sw": {-0.75, -0.5}}
	var maxDist float64

	for _, direction := range path {
		x_move, y_move := dirs[direction][0], dirs[direction][1]

		pos[0] += x_move
		pos[1] += y_move

		dist := distFromStart(pos)
		if dist > maxDist {
			maxDist = dist
		}
	}

	return pos, maxDist
}

func parse(inputFile string) []string {
	inputData := util.FileToStr(inputFile)
	path := strings.Split(inputData, ",")
	
	return path
}

func abs(num float64) float64 {
	if num < 0 {
		return -num
	}

	return num
}