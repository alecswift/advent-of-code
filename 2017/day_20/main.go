// Puzzle explanation: https://adventofcode.com/2017/day/20

package main

import (
	"fmt"
	"regexp"

	"github.com/alecswift/advent_of_code/stringOps"
	"github.com/alecswift/advent_of_code/util"
)

func main() {
	particles := parse("/home/alec/Desktop/code/advent-of-code/2017/day_20/input.txt")
	part1Sol := part1(particles)
	fmt.Print(part1Sol, "\n")
	particlesMap := initParticlesMap(particles)

	for i := 0; i < 40; i++ {
		particlesMap = updateParticlesMap(particlesMap)
	}
	fmt.Print(len(particlesMap))
}

func updateParticlesMap(particlesMap map[[3]int][9]int) map[[3]int][9]int {
	newMap := make(map[[3]int][9]int)
	collided := make(map[[3]int]bool)

	for _, particle := range particlesMap {
		particle := updateState(particle)
		pos := [3]int{particle[0], particle[1], particle[2]}
		_, exists := newMap[pos]
		if exists {
			collided[pos] = true
		}
		newMap[pos] = particle
	}

	for pos := range collided {
		delete(newMap, pos)
	}
	
	return newMap
}

func initParticlesMap(particles [][9]int) map[[3]int][9]int {
	particlesMap := make(map[[3]int][9]int)

	for _, particle := range particles {
		pos := [3]int{particle[0], particle[1], particle[2]}
		_, exists := particlesMap[pos]
		if exists {
			delete(particlesMap, pos)
		} else {
			particlesMap[pos] = particle
		}
	}
	
	return particlesMap
}

func part1(particles [][9]int) int {
	var mins, minIdxs []int
	mins = append(mins, 0)

	for idx, particle := range particles {
		acc := abs(particle[6]) + abs(particle[7]) + abs(particle[8])
		if acc == mins[0] {
			mins = append(mins, acc)
			minIdxs = append(minIdxs, idx)
		} else if mins[0] == 0 || acc < mins[0] {
			mins = []int{acc}
			minIdxs = []int{idx}
		}
	}

	particle := particles[minIdxs[0]]
	part1Sol := abs(particle[0]) + abs(particle[1]) + abs(particle[2])

	for i := 1; i < len(minIdxs); i++ {
		particle := particles[minIdxs[i]]
		dist := abs(particle[0]) + abs(particle[1]) + abs(particle[2])
		if dist < part1Sol {
			part1Sol = minIdxs[i]
		}
	}
	return part1Sol
}

func abs(num int) int {
	if num > 0 {
		return num
	}

	return -num
}

func updateState(particle [9]int) [9]int {
	particle[3] += particle[6]
	particle[4] += particle[7]
	particle[5] += particle[8]
	
	particle[0] += particle[3]
	particle[1] += particle[4]
	particle[2] += particle[5]

	return particle
}

func parse(inputFile string) [][9]int {
	data := util.FileToStr(inputFile)
	re := regexp.MustCompile(`[-0-9]+`)
	rawNums := re.FindAllString(data, -1)
	particles := [][9]int{}
	var particle [9] int

	for i := 0; i < len(rawNums); i++ {
		if i != 0 && i % 9 == 0 {
			particles = append(particles, particle)
			particle = [9]int{}
		}
		
		currNum := stringOps.StrToInt(rawNums[i])
		particle[i % 9] = currNum
	}
	particles = append(particles, particle)
	particle = [9]int{}

	return particles
}
