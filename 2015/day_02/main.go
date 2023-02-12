// Puzzle explanation: https://adventofcode.com/2015/day/2#part2

package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

func main() {
	boxes := parse("2015/day_2/input.txt")
	totalMaterials := calcMaterials(boxes)
	paper := totalMaterials[0]
	ribbon := totalMaterials[1]
	fmt.Printf(
		"The elves must order %d square feet of wrapping paper and %d feet of ribbon",
		paper, ribbon)
}

func parse(inputFile string) [][3]int {
	data, err := os.ReadFile(inputFile)
	if err != nil {
		log.Fatal(err)
	}
	inputData := string(data)
	split_lines := regexp.MustCompile("\n").Split(inputData, -1)

	var boxes [][3]int
	for _, item := range split_lines {
		// Split each line into the 3 dimensions length x width x height.
		temp := regexp.MustCompile("x").Split(item, 3)
		var box [3]int
		// Convert all dimensions from strings to integers.
		for index, str_num := range temp {
			num, err := strconv.Atoi(str_num)
			if err != nil {
				log.Fatal(err)
			}
			box[index] = num
		}
		boxes = append(boxes, box)
	}
	return boxes
}

func calcMaterials(boxes [][3]int) [2]int {
	totalPaper := 0
	totalRibbon := 0
	for _, box := range boxes {
		box := sortDimensions(box[0], box[1], box[2])
		// Total wrapping paper found by adding the total surface area
		// and the surface area of the smallest side
		smallSide := box[1] * box[2]
		side_2 := box[0] * box[1]
		side_3 := box[0] * box[2]
		totalPaper += 2*smallSide + 2*side_2 + 2*side_3
		totalPaper += smallSide
		// Total ribbon found by adding the volume and the smallest perimeter
		totalRibbon += box[0] * box[1] * box[2]
		totalRibbon += box[1]*2 + box[2]*2
	}
	return [2]int{totalPaper, totalRibbon}
}

func sortDimensions(num_1 int, num_2 int, num_3 int) [3]int {
	// Return the slice with the largest number in the zero index of a slice
	if num_2 <= num_1 && num_3 <= num_1 {
		return [3]int{num_1, num_2, num_3}
	} else if num_1 <= num_2 && num_3 <= num_2 {
		return [3]int{num_2, num_1, num_3}
	}
	return [3]int{num_3, num_1, num_2}

}
