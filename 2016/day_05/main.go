package main

import (
	"crypto/md5"
	"fmt"
	"encoding/hex"
	"io"
	"strconv"
	"strings"
	"unicode/utf8"
)

func main() {
	doorID := "reyedfim"
	fmt.Print("Initializing password for door 2...\n")
	password := findPassword(doorID, 0)
	fmt.Printf("Password for door 1: %s", password)
}

func findPassword(doorID string, idx int) string {
	password := ""
	password2 := []string{"_","_","_","_","_","_","_","_"}
	for isNotFilled(password2) {
		hash := makeHash(doorID, idx)
		for !(hash[0] == 0 && hash[1] == 0 && hash[2] <= 15) {
			hash = makeHash(doorID, idx)
			idx++
		}
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

func makeHash(key string, num int) []byte {
	numStr := strconv.Itoa(num)
	hash := md5.New()
	io.WriteString(hash, key)
	io.WriteString(hash, numStr)
	return hash.Sum(nil)
}