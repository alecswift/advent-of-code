package main

import (
	"encoding/hex"
	"fmt"
	"strings"

	"github.com/alecswift/advent_of_code/arrayOps"
	"github.com/alecswift/advent_of_code/util"
)

func main() {
	inputData := util.FileToStr("/home/alec/Desktop/code/advent-of-code/2017/day_10/input.txt")
	lengthsStr := strings.Split(inputData, ",")
	lengths := arrayOps.StrListToIntList(lengthsStr)
	nums := genNums()


	hashList(nums, lengths, 0, 0)
	part1 := nums[0] * nums[1]
	fmt.Print(part1, "\n")

	nums = genNums()
	byteLengths := []byte(inputData)
	extraBytes := []byte{17, 31, 73, 47, 23}
	byteLengths = append(byteLengths, extraBytes...)
	
	hexString := part2(nums, byteLengths)
	fmt.Print(hexString)
}

func part2(nums []int, byteLengths []byte) string {
	pos := 0
	skipSize := 0
	lengths := make([]int, len(byteLengths))

	for i, b := range byteLengths {
		lengths[i] = int(b)
	}


	for i := 0; i < 64; i++ {
		pos = hashList(nums, lengths, pos, skipSize)
		skipSize += len(lengths)
	}

	hash := make([]byte, 16)

	var newNum int
	newIdx := 0
	for idx, num := range nums {
		if idx == 0 {
			newNum += num
		} else if idx % 16 == 0 {
			hash[newIdx] = byte(newNum)
			newNum = 0
			newNum += num
			newIdx++
		} else {
			newNum ^= num
		}
	}

	hash[newIdx] = byte(newNum)
	hexString := hex.EncodeToString(hash)

	return hexString
}


func hashList(nums, lengths []int, pos, skipSize int) int {
	for _, length := range lengths {
		end := (pos + length) % len(nums)

		arrayOps.ReverseFrom(nums, pos, end)
		pos += (length + skipSize)
		pos %= len(nums)
		skipSize++
	}
	return pos
}

func genNums() []int {
	nums := make([]int, 256)

	for i := 0; i < 256; i++ {
		nums[i] = i
	}

	return nums
}