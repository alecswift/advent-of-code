package hashList

import (

	
)
func part2(nums []int, byteLengths []byte) string {
	pos := 0
	skipSize := 0
	lengths := make([]int, len(byteLengths))

	for i, b := range byteLengths {
		lengths[i] = int(b)
	}


	for i := 0; i < 64; i++ {
		pos = hashList(nums, lengths, pos, skipSize)
		skipSize += len(lengths)
	}

	hash := make([]byte, 16)

	var newNum int
	newIdx := 0
	for idx, num := range nums {
		if idx == 0 {
			newNum += num
		} else if idx % 16 == 0 {
			hash[newIdx] = byte(newNum)
			newNum = 0
			newNum += num
			newIdx++
		} else {
			newNum ^= num
		}
	}

	hash[newIdx] = byte(newNum)
	hexString := hex.EncodeToString(hash)

	return hexString
}


func hashList(nums, lengths []int, pos, skipSize int) int {
	for _, length := range lengths {
		end := (pos + length) % len(nums)

		arrayOps.ReverseFrom(nums, pos, end)
		pos += (length + skipSize)
		pos %= len(nums)
		skipSize++
	}
	return pos
}