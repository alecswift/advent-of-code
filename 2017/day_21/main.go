// Puzzle explanation: https://adventofcode.com/2017/day/21

package main

import (
	"fmt"
	"math"
	"math/bits"
	"regexp"

	"github.com/alecswift/advent_of_code/util"
)

func main() {
	rules4, rules9 := parse("/home/alec/Desktop/code/advent-of-code/2017/day_21/input.txt")
	fmt.Print(rules4, "\n", len(rules4))
	fmt.Print("\n", rules9, "\n", len(rules9))
}

func split4by4(bits16 uint) []uint {
	out := []uint{}
	return out
}

func flipVert4(bits4 uint) uint {
	return (bits4 << 2) | (bits4 >> 2)
}

func flipHor4(bits4 uint) uint {
	evenMask := 5
	oddMask := 10

	evenBits := bits4 & uint(oddMask)
	oddBits := bits4 & uint(evenMask)

	swapped := (evenBits << 1) | (oddBits >> 1)

	return swapped
}

func flipDiag4(bits4 uint) uint {
	midBits := bits4 & 6
	endBits := bits4 & 9
	out := midBits | bits.Reverse(endBits)
	return out
}

func flipVert9(bits9 uint) uint {
	return (bits9 << 6) | (bits9 & 56)| (bits9 >> 6)
}

func flipHor9(bits9 uint) uint {
	return (bits.Reverse(bits9 >> 6) << 6) | (bits.Reverse((bits9 & 56) >> 3) << 3) | bits.Reverse(bits9 & 7)
}

func flipDiag9(bits9 uint) uint {
	out := 0
	if bits9 & 256 != 0 {
		out += 1
	}
	if bits9 & 32 != 0 {
		out += 2
	}
	if bits9 & 4 != 0 {
		out += 4
	}
	if bits9 & 128 != 0 {
		out += 8
	}
	if bits9 & 16 != 0 {
		out += 16
	}
	if bits9 & 2 != 0 {
		out += 32
	}
	if bits9 & 64 != 0 {
		out += 64
	}
	if bits9 & 8 != 0 {
		out += 128
	}
	if bits9 & 1 != 0 {
		out += 256
	}
	return uint(out)
}

func rotate4(bit4 uint) uint {
	return flipVert4(flipDiag4(bit4))
}

func rotate9(bit9 uint) uint {
	return flipVert9(flipDiag9(bit9))
}

func parse(inputFile string) (map[uint]uint, map[uint]uint) {
	rawData := util.FileToStr(inputFile)
	re := regexp.MustCompile(`[.#/]+`)
	data := re.FindAllString(rawData, -1)
	rules4 := make(map[uint]uint)
	rules9 := make(map[uint]uint)

	for i := 0; i < len(data); i += 2 {
		match, conversion := strToBits(data[i]), strToBits(data[i + 1])
		if len(data[i]) == 5 {
			rules4[match] = conversion
		} else {
			rules9[match] = conversion
		}
	}

	return rules4, rules9
}

func strToBits(str string) uint {
	var out uint
	exponent := len(str) - (int(math.Log2(float64(len(str)))))

	for _, char := range str {
		if char == '/' { continue }
		if char == '#' {
			out += uint(math.Pow(2, float64(exponent)))
		}
		exponent -= 1
	}

	return out
}