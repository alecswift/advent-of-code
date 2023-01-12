// Puzzle explanation: https://adventofcode.com/2015/day/4

package main

import (
	"crypto/md5"
	"fmt"
	"io"
	"strconv"
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
	hash := makeHash(key, num)
	// first 3 bytes must be less than 16 or 0 equivalent to 000010 or 000000 in hex
	for !(hash[0] == 0 && hash[1] == 0 && hash[2] <= condition) {
		num++
		hash = makeHash(key, num)
	}
	return num
}

func makeHash(key string, num int) []byte {
	numStr := strconv.Itoa(num)
	hash := md5.New()
	io.WriteString(hash, key)
	io.WriteString(hash, numStr)
	return hash.Sum(nil)
	// make this return a different type?
}
