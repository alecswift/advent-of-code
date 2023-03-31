package main

import (
	"fmt"
	"strings"

	"github.com/alecswift/advent_of_code/arrayOps"
	"github.com/alecswift/advent_of_code/util"
)

const Length = 16

func main() {
	cache := make(map[[Length]int]bool)
	banks := parse("/home/alec/Desktop/code/advent_of_code/2017/day_6/input.txt")
	cycles := part1(banks, cache)
	fmt.Print(cycles)
}

func part1(banks [Length]int, cache map[[Length]int]bool) int {
	var initialCycles int
	_, exists := cache[banks]

	for !exists {
		maxIdx := maxBlock(banks)
		redistribute(&banks, maxIdx)
		_, exists = cache[banks]
		cache[banks] = true
		initialCycles++
	}
	
	return initialCycles
}

func redistribute(banks *[Length]int, maxIdx int) {
	blocks := banks[maxIdx]
	length := len(banks)
	banks[maxIdx] = 0

	for idx := maxIdx + 1; blocks > 0; idx++ {
		idx %= length

		banks[idx]++
		blocks--
	}
}

func maxBlock(banks [Length]int) int {
	maxNum := 0
	maxIdx := 0

	for idx, num := range banks {
		if num > maxNum {
			maxNum = num
			maxIdx = idx
		}
	}
	
	return maxIdx
}

func parse(fileName string) [Length]int {
	data := util.FileToStr(fileName)
	split_lines := strings.Split(data, "\t")
	banksSlc := arrayOps.StrListToIntList(split_lines)
	var banks [Length]int
	copy(banks[:], banksSlc)
	return banks
}