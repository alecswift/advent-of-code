package main

import "fmt"

func main() {
	target := 36000000
	fmt.Print(findHouse(target, true), "\n")
	fmt.Print(findHouse(target, false))
}

func findHouse(target int, part1 bool) int {
	houses := map[int]int{}
	maxRange := target / 25
	multiplier := 10
	for elf := 1; elf < maxRange; elf ++ {
		if !part1 {
			maxRange = elf * 51
			multiplier = 11
		}
		for house := elf; house < maxRange; house += elf {
			_, exists := houses[house]
			if exists {
				houses[house] += elf * multiplier
			} else {
				houses[house] = elf * multiplier
			}
		}
		if target <= houses[elf] {
			return elf
		}
		delete(houses, elf)
	}
	return -1
}
