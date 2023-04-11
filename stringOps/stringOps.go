package stringOps

import (
	"strconv"
)

func StrToInt(numStr string) int {
	num, err := strconv.Atoi(numStr)

	if err != nil {
		panic(err)
	}

	return num
}