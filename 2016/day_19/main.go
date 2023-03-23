package main

import (
	"math"
	"fmt"
)
func main() {
	input := 3014387
	part1Sol := part1(input)
	fmt.Print(part1Sol, "\n")
	part2Sol := part2(input)
	fmt.Print(part2Sol)
}

func part1(input int) int {
	power_of_2_exp := math.Floor(math.Log2(float64(input)))
	power_of_2 := int(math.Pow(2, power_of_2_exp))
	return ((input - power_of_2) * 2) + 1
}

func part2(input int) int {
	powerOfThree := int(math.Pow(3, math.Floor(logb(float64(input), 3))))
    winForElf1 := input - int(powerOfThree)
    if input == powerOfThree {
		return powerOfThree
	} else if winForElf1 < powerOfThree {
        return winForElf1
	} else {
		return winForElf1 * 2 - powerOfThree
	}
}

func logb(num, base float64) float64 {
	return math.Log(num) / math.Log(base)
}