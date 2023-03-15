// Puzzle explanation: https://adventofcode.com/2016/day/14

package main

import (
	"crypto/md5"
	"fmt"
	"encoding/hex"
	"io"
	"strconv"
)

func main() {
	salt := "zpqevtbw"
	idx := find64thkey(salt, nil)
	cache := map[int]string{}
	initial_hash := makeHash(salt, 0)
	initial_hash = stretchHash(initial_hash)
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
			hash = makeHash(salt, idx)
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
			hash = makeHash(salt, idx + i)
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
		hash = makeHash(salt, idx)
		hash = stretchHash(hash)
		cache[idx] = hash
	}
	return hash
}


func findThreeSequence(hash string) (bool, rune) {
	// am I looking for sequences of exactly 3?
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

func makeHash(key string, idx int) string {
	numStr := strconv.Itoa(idx)
	hash := md5.New()
	io.WriteString(hash, key)
	io.WriteString(hash, numStr)
	return hex.EncodeToString(hash.Sum(nil))
}

func stretchHash(hash string) string {
	for i := 0; i < 2016; i++ {
		newHash := md5.New()
		io.WriteString(newHash, hash)
		hash = hex.EncodeToString(newHash.Sum(nil))
	}
	return hash
}
