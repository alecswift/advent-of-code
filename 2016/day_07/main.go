package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Print(parse("2016/day_07/input.txt"))
}

func parse(inputFile string) []string {
	inFile, err := os.ReadFile(inputFile)
	if err != nil {
		panic(err)
	}
	data := strings.Split(string(inFile), "\n")
	return data
}