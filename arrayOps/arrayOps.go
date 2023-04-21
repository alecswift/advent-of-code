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
	var revSeg []T

	if start < end {
		revSeg = reverse(seq[start: end])

		copy(seq[start: end], revSeg)
	} else if start > end {
		revSeg = reverse(seq[:end])
		revSeg = append(revSeg, reverse(seq[start:])...)

		copy(seq[start:], revSeg[:len(seq) - start])
		copy(seq[:end], revSeg[len(seq) - start:])
	}
}

func reverse[T any] (seq []T) []T {
	var rev []T

	for i := len(seq) - 1; i >= 0; i-- {
		rev = append(rev, seq[i])
	}

	return rev
}

func Insert[T any] (seq []T, idx int, val T) []T {
	if idx == len(seq) {
		seq = append(seq, val)
	} else {
		seq = append(seq[:idx + 1], seq[idx:]...)
		seq[idx] = val
	}

	return seq
}