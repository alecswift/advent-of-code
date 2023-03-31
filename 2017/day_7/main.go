package main

import (
	"fmt"
	"regexp"
	"strings"

	"github.com/alecswift/advent_of_code/util"
)

type Node struct {
	name     string
	weight   int
	parent   *Node
	children []*Node
}

func main() {
	parse("/home/alec/Desktop/code/advent_of_code/2017/day_7/input.txt")
}

func parse(fileName string) {
	data := util.FileToStr(fileName)
	splitLines := strings.Split(data, "\n")
	nodes := make(map[string]*Node)

	for _, line := range splitLines {
		re := regexp.MustCompile("[a-z0-9]+")
		nodeData := re.FindAllString(line, -1)
		// fmt.Print(nodeData, "\n")
		isLeaf := len(nodeData) == 2

		if isLeaf {
			
		}
	}
}