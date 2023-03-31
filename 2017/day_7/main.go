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
	nodes := parse("/home/alec/Desktop/code/advent_of_code/2017/day_7/input.txt")
	var node *Node
	for _, randNode := range nodes {
		node = randNode
	}
	root := findRoot(node)
	fmt.Print(root.name)
}

func findRoot(node *Node) *Node {
	if node.parent == nil {
		return node
	}
	return findRoot(node.parent)
}

func parse(fileName string) map[string]*Node {
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

		if isLeaf {
			_, exists := nodes[name]

			if exists {
				nodes[name].weight = weight
			} else {
				newNode := Node{
					name: name,
					weight: weight,
				}
				nodes[name] = &newNode
			}
			
		} else {
			chNames := nodeData[2:]
			chNodes := []*Node{}


			for _, chName := range chNames {
				_, exists := nodes[chName]
				var chNode Node

				if exists {
					pChNode, _ := nodes[chName]
					chNodes = append(chNodes, pChNode)
				} else {
					chNode = Node {
						name: chName,
					}
					chNodes = append(chNodes, &chNode)
					nodes[chName] = &chNode
				}
			}

			var pNewNode *Node
			_, exists := nodes[name]

			if exists {
				pNewNode, _ = nodes[name]
			} else {
				newNode := Node{
					name: name,
					weight: weight,
					children: chNodes,
				}
				pNewNode = &newNode
			}

			for _, chNode := range chNodes {
				chNode.parent = pNewNode
			}

			nodes[name] = pNewNode
		}
	}

	return nodes
}

