// Puzzle explanation: https://adventofcode.com/2017/day/10

package main

import (
	"fmt"
	"strings"

	"github.com/alecswift/advent_of_code/arrayOps"
	"github.com/alecswift/advent_of_code/2017/hashList"
	"github.com/alecswift/advent_of_code/util"
)

func main() {
	inputData := util.FileToStr("/home/alec/Desktop/code/advent-of-code/2017/day_10/input.txt")
	lengthsStr := strings.Split(inputData, ",")
	lengths := arrayOps.StrListToIntList(lengthsStr)
	nums := genNums()


	hashList.HashList(nums, lengths, 0, 0)
	part1 := nums[0] * nums[1]
	fmt.Print(part1, "\n")

	nums = genNums()
	byteLengths := []byte(inputData)
	extraBytes := []byte{17, 31, 73, 47, 23}
	byteLengths = append(byteLengths, extraBytes...)
	
	hexString := hashList.Part2Hash(nums, byteLengths)
	fmt.Print(hexString)
}

func genNums() []int {
	nums := make([]int, 256)

	for i := 0; i < 256; i++ {
		nums[i] = i
	}

	return nums
}