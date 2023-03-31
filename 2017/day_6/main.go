package main

import (
	"fmt"
	"reflect"
	"strings"

	"github.com/alecswift/advent_of_code/arrayOps"
	"github.com/alecswift/advent_of_code/util"
)

const Length = 16

func main() {
	cache := make(map[[Length]int]bool)
	banks := parse("/home/alec/Desktop/code/advent_of_code/2017/day_6/input.txt")
	part1, part2  := solution(banks, cache)
	fmt.Print(part1, "\n", part2)
}

func solution(banks [Length]int, cache map[[Length]int]bool) (int, int) {
	var initialCycles int
	_, exists := cache[banks]

	for !exists {
		maxIdx := maxBlock(banks)
		redistribute(&banks, maxIdx)
		_, exists = cache[banks]
		cache[banks] = true
		initialCycles++
	}

	cycles := initialCycles
	target := banks

	for true {
		maxIdx := maxBlock(banks)
		redistribute(&banks, maxIdx)
		cycles++
		
		if reflect.DeepEqual(banks, target) {
			break
		}
	}
	
	return initialCycles, cycles - initialCycles
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