package main

import (
	"fmt"
	"os"
)

func main() {
	directions := parse("2015/day_3/input.txt")
	santa, robotAndSanta := deliverPresents(directions)
	fmt.Printf("Santa delivers presents to %d presents on his own\n", santa)
	fmt.Printf("With the excellent help of robot santa, they deliver %d presents", robotAndSanta)
}

func parse(inputFile string) string {
	inputData, err := os.ReadFile(inputFile)
	if err != nil {
		panic(err)
	}
	return string(inputData)
}

func deliverPresents(directions string) (int, int){
	pos := complex(0, 0)
	houses := map[complex128]bool{pos: true}
	moves := map[rune]complex128{
		'^': complex(0, 1),
		'v': complex(0, -1),
		'>': complex(1, 0),
		'<': complex(-1, 0),
	}
	// Move only one object (pos)
	for _, direction := range directions {
		pos += moves[direction]
		_, visited := houses[pos]
		if !visited {
			houses[pos] = true
		}
	}
	// Now we move two objects (santaPos, robotPos) that take turns each direction
	santaPos := complex(0, 0)
	robotPos := complex(0, 0)
	houses_2 := map[complex128]bool{santaPos: true}
	for idx, direction := range directions {
		if idx % 2 == 0 {
			santaPos += moves[direction]
			_, visited := houses_2[santaPos]
			if !visited {
				houses_2[santaPos] = true
			}
		} else {
			robotPos += moves[direction]
			_, visited := houses_2[robotPos]
			if !visited {
				houses_2[robotPos] = true
			}
		}
	}
	return len(houses), len(houses_2)
}