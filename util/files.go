package util

import (
	"os"
	"strings"
)

func FileToStr(inputFile string) string {
	inputData, err := os.ReadFile(inputFile)
	if err != nil {
		panic(err)
	}
	return strings.Trim(string(inputData), "\n")
}