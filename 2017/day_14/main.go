package main

import (
	"fmt"
	"encoding/hex"
	"strconv"

	"github.com/alecswift/advent_of_code/2017/hashList"
)

func main() {
	input := "wenycdww"
	byteInput := []byte(input)
	byteInput = append(byteInput, '-')

	part1Sol := part1(byteInput)
	fmt.Print(part1Sol)
}

func part1(byteLengths []byte) int {
	total := 0

	for i := 0; i < 128; i++ {
		nums := genNums()
		hash := makeHash(byteLengths, nums, i)
		bytes, err := hex.DecodeString(hash)
		if err != nil {
			panic(err)
		}

		for _, byte_ := range bytes {
			total += countSet(byte_)
		}
	}

	return total
}

func countSet(byte_ byte) int {
	count := 0

	for byte_ != 0 {
		count += int(byte_ & 1)
		byte_ >>= 1
	}

	return count
}

func makeHash(byteLengths []byte, nums []int, num int) string {
	numStr := strconv.Itoa(num)
	byteLengths = append(byteLengths, []byte(numStr)...)
	extraBytes := []byte{17, 31, 73, 47, 23}
	byteLengths = append(byteLengths, extraBytes...)

	hexString := hashList.Part2Hash(nums, byteLengths)
	return hexString
}

func genNums() []int {
	nums := make([]int, 256)

	for i := 0; i < 256; i++ {
		nums[i] = i
	}

	return nums
}