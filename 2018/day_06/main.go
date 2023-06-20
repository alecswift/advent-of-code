package main

import (
	"fmt"
	"strings"

	"github.com/alecswift/advent_of_code/stringOps"
	"github.com/alecswift/advent_of_code/util"
)

type Coord struct{
	row int
	col int
}

func main() {
	coords := parse("/home/alec/Desktop/code/advent-of-code/2018/day_06/input.txt")
	fmt.Print(coords)
}

func parse(inputFile string) []Coord {
	data := util.FileToStr(inputFile)
	splitLines := strings.Split(data, "\n")
	coords := []Coord{}

	for _, line := range splitLines {
		raw := strings.Split(line, ", ")
		coord := Coord{
			row: stringOps.StrToInt(raw[1]),
			col: stringOps.StrToInt(raw[0]),
		}
		coords = append(coords, coord)
	}

	return coords
}
