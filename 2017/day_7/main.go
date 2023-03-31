package main

import (
	"fmt"
	"strconv"
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

func findRoot(node *Node) *Node {
	panic("nobody")
}

func parse(fileName string) {
	data := util.FileToStr(fileName)
	splitLines := strings.Split(data, "\n")
	nodes := make(map[string]*Node)

	for _, line := range splitLines {
		re := regexp.MustCompile("[a-z0-9]+")
		nodeData := re.FindAllString(line, -1)
		isLeaf := len(nodeData) == 2
		name, weightStr := nodeData[0], nodeData[1]

		weight, err := strconv.Atoi(weightStr)
		if err != nil {
			panic("Error")
		}

		fmt.Print(nodeData, "\n")

		if isLeaf {
			newNode := Node{
				name: name,
				weight: weight,
			}
			// possibly check for membership in dict first
			// might not have to do this for leafs, i think I do so I don't erase the parent data member
			// Also look up struct info to see if you need to initialize every data member
			nodes[name] = &newNode
		} else {
			panic("nobody")
		}
	}
}