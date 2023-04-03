// Puzzle explanation: https://adventofcode.com/2017/day/8

package main

import (
	"fmt"
	"regexp"
	"strconv"
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
	fmt.Print(root.name, "\n")
	part2 := findImbalance(root)
	fmt.Print(part2)
}

func findImbalance(root *Node) int {
	type Counter struct{
		count int
		nodes []*Node
	}
	stws := make(map[int]Counter)

	for _, child := range(root.children) {
		weight := 0
		subTreeWeight(child, &weight)

		counter := stws[weight]

		counter.count++
		counter.nodes = append(counter.nodes, child)
		stws[weight] = counter
	}

	// If the rest of the subtrees are weight balanced end recursive calls
	if len(stws) == 1 {
		return -1
	}


	var incorrect_stw int
	var correct_stw int
	var incorrect_node *Node

	for stw, counter := range stws {
		if counter.count == 1 {
			incorrect_stw = stw
			incorrect_node = counter.nodes[0]
		} else {
			correct_stw = stw
		}
	}

	solution := findImbalance(incorrect_node)

	// if it's the last imbalanced subtree calculate the solution
	if solution == -1 {
		solution = incorrect_node.weight + (correct_stw - incorrect_stw)
	}

	return solution
}

func subTreeWeight(node *Node, weight *int) {
	for _, child := range node.children {
		subTreeWeight(child, weight)
	}
	*weight += node.weight
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
				}
				pNewNode = &newNode
			}

			pNewNode.weight = weight
			pNewNode.children = chNodes

			for _, chNode := range chNodes {
				chNode.parent = pNewNode
			}

			nodes[name] = pNewNode
		}
	}

	return nodes
}
