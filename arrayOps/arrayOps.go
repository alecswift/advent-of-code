package arrayOps

import (
	"strconv"
)

func Remove(arr []string, idx int) []string {
	arr[idx] = arr[len(arr) - 1]
	return arr[:len(arr) - 1]
}

func StrListToIntList(seq []string) []int {
	nums := []int{}
	for _, line := range seq {
		num, err := strconv.Atoi(line)

		if err != nil {
			panic("Error")
		}

		nums = append(nums, num)
	}

	return nums
}

func Rotate(seq []string, steps, direction int) []string {
	/* 
	rotate an array a given number of steps in the specified direction
	1 = right, -1 = left
	*/
	length := len(seq)
	if direction == 1 {
		for ;0 < steps; steps-- {
			seq = append(seq[length - 1:], seq[0:length - 1]...)
		}
	} else {
		for ;0 < steps; steps-- {
			seq = append(seq[1: length], seq[0])
		}
	}
	return seq
}

func ReverseFrom[T any] (seq []T, start, end int) {
	/*
	Reverse the given sequence from position start to position end
	*/
	if start > end {
		lengthToRev := (len(seq) - start) + end + 1
		endCond := int(lengthToRev / 2)

		for i := 0; i < endCond; start, end, i = start + 1, end - 1, i + 1 {
			end %= len(seq)
			start %= len(seq)
			seq[start], seq[end] = seq[end], seq[start]
		}

	} else {

		for ; start <= end; start, end = start + 1, end - 1 {
			seq[start], seq[end] = seq[end], seq[start]
		}

	}
}

func abs(num int) int {
	if num < 0 {
		return -num
	}

	return num
}