// Puzzle explanation: https://adventofcode.com/2015/day/4

package main

import (
	"fmt"
	"github.com/alecswift/advent_of_code/md5"
)

func main() {
	key := "yzbqklnj"
	hash := findHash(key, 15)
	hash_2 := findHash(key, 0)
	fmt.Printf("Here's an MD5 hash that starts with 5 zeroes for your key: %d\n", hash)
	fmt.Printf("Here's one that starts with 6 zeroes: %d", hash_2)
}

func findHash(key string, condition byte) int {
	num := 1
	hash := md5.HashWithIdxToBytes(key, num)
	// first 3 bytes must be less than 16 or 0 equivalent to 000010 or 000000 in hex
	for !(hash[0] == 0 && hash[1] == 0 && hash[2] <= condition) {
		num++
		hash = md5.HashWithIdxToBytes(key, num)
	}
	return num
}
