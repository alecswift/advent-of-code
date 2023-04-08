package main

import (
	"strings"

	"github.com/alecswift/advent_of_code/stringOps"
	"github.com/alecswift/advent_of_code/util"
)

func main() {
	panic("err")
}


func parse(inputFile string) {
	inputData := util.FileToStr(inputFile)
	splitLines := strings.Split(inputData, "\n")
	things := make([][]int, 98)

	for _, line := range splitLines {
		data := strings.Split(line, ": ")
		depth := stringOps.strToInt(data[0])
		fRange := stringOps.strToInt(data[1])

	}
}