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
	x := findInbalance(root)
	fmt.Print(x)
}

func findInbalance(root *Node) int {
	type QueueNode struct {
		node  *Node
		depth int
	}
	var prevDepth int
	var solution int
	start := QueueNode{
		node: root,
		depth: 0,
	}
	queue := []QueueNode{start}

	for len(queue) > 0 {
		currNode := queue[0].node
		currDepth := queue[0].depth
		if prevDepth < currDepth {
			prevDepth++
			fmt.Print(" x\n")
		}


		type Counter struct{
			count int
			nodes []*Node
		}
		stws := make(map[int]Counter)

		for _, child := range(currNode.children) {
			weight := 0
			subTreeWeight(child, &weight)
			fmt.Print(weight, " ")

			counter := stws[weight]

			counter.count++
			counter.nodes = append(counter.nodes, child)
			stws[weight] = counter

			queueNode := QueueNode{
				node: child,
				depth: currDepth + 1,
			}
			queue = append(queue, queueNode)
		}

		if len(stws) == 1 { // wrong!!!
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

		findInbalance(incorrect_node)

		solution = incorrect_node.weight + (correct_stw - incorrect_stw)
		return solution
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

