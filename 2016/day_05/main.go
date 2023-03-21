// Puzzle explanation: https://adventofcode.com/2016/day/5

package main

import (
	"fmt"
	"encoding/hex"
	"strconv"
	"strings"
	"unicode/utf8"
	"github.com/alecswift/advent_of_code/md5"
)

func main() {
	doorID := "reyedfim"
	fmt.Print("Initializing password for door 2...\n")
	password := findPassword(doorID, 0)
	fmt.Printf("\nPassword for door 1: %s", password)
}

func findPassword(doorID string, idx int) string {
	password := ""
	password2 := []string{"_","_","_","_","_","_","_","_"}
	for isNotFilled(password2) {
		hash := md5.HashWithIdxToBytes(doorID, idx)
		for !(hash[0] == 0 && hash[1] == 0 && hash[2] <= 15) {
			hash = md5.HashWithIdxToBytes(doorID, idx)
			idx++
		}
		// part 1
		hexHash := hex.EncodeToString(hash)
		if utf8.RuneCountInString(password) < 8 {
			password += string(hexHash[5])
		}
		// part 2
		pos, err := strconv.Atoi(string(hexHash[5]))
		if err == nil && pos < 8 && password2[pos] == "_" { 
			password2[pos] = string(hexHash[6])
			fmt.Print(strings.Join(password2, ""), "\n")
		}
	}
	return password
}

func isNotFilled(password2 []string) bool {
	for _, char := range password2 {
		if char == "_" {
			return true
		}
	}
	return false
}
