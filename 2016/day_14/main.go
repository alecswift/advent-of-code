// Puzzle explanation: https://adventofcode.com/2016/day/14

package main

import (
	"fmt"
	"github.com/alecswift/advent_of_code/md5"
)

func main() {
	salt := "zpqevtbw"
	idx := find64thkey(salt, nil)
	cache := map[int]string{}
	initial_hash := md5.HashWithIdxToString(salt, 0)
	initial_hash = md5.StretchHash(initial_hash, 2016)
	cache[0] = initial_hash
	idx2 := find64thkey(salt, cache)
	fmt.Printf("%d\n", idx)
	fmt.Printf("%d\n", idx2)
}

func find64thkey(salt string, cache map[int]string) int {
	var hash string
	idx := 0
	keyNum := 0
	for keyNum < 64 {
		if cache != nil {
			hash = searchCache(salt, cache, idx)
		} else {
			hash = md5.HashWithIdxToString(salt, idx)
		}
		hasTriplet, char := findThreeSequence(hash)
		if hasTriplet {
			isKey := lookForward(salt, char, idx, cache)
			if isKey { keyNum++ }
		}
		idx++
	}
	return idx - 1
}

func lookForward(salt string, char rune, idx int, cache map[int]string) bool {
	var hash string
	for i := 1; i < 1001; i++ {
		if cache != nil {
			hash = searchCache(salt, cache, idx + i)
		} else {
			hash = md5.HashWithIdxToString(salt, idx + i)
		}
		if findFiveSequence(hash, char) {
			return true
		}
	}
	return false
}

func searchCache(salt string, cache map[int]string, idx int) string {
	hash, exists := cache[idx]
	if !exists {
		hash = md5.HashWithIdxToString(salt, idx)
		hash = md5.StretchHash(hash, 2016)
		cache[idx] = hash
	}
	return hash
}


func findThreeSequence(hash string) (bool, rune) {
	var lastDigit rune
	count := 1
	for _, hexDigit := range hash {
		if hexDigit == lastDigit {
			count += 1
		} else {
			count = 1
		}
		if count == 3 {
			return true, lastDigit
		}
		lastDigit = hexDigit
	}
	return false, lastDigit
}

func findFiveSequence(hash string, char rune) bool {
	// again looking for exactly 5 or just 5?
	count := 0
	for _, hexDigit := range hash {
		if hexDigit == char {
			count += 1
		} else {
			count = 0
		}
		if count == 5 {
			return true
		}
	}
	return false
}
