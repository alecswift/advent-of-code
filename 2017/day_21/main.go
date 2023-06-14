// Puzzle explanation: https://adventofcode.com/2017/day/21

package main

import (
	"fmt"
	"math"
	"regexp"

	"github.com/alecswift/advent_of_code/util"
)

func main() {
	rules4, rules9 := parse("/home/alec/Desktop/code/advent-of-code/2017/day_21/input.txt")
	//fmt.Print(rules4, "\n", len(rules4))
	//fmt.Print("\n", rules9, "\n", len(rules9))
	
	start := []uint{143}
	end := iterate(start, rules9, rules4)
	count := countSet(end)
	fmt.Print(count)
}

func countSet(picture []uint) uint {
	var count uint

	for _, num := range picture {
		for ;num != 0; num >>= 1 {
			count += num & 1
		}
	}

	return count
}

func iterate(picture []uint, rules9, rules4 map[uint]uint) []uint {
	size := 3

	for i := 0; i < 18; i++ {
		if size % 2 == 0 {
			bits := int(math.Pow(float64(size), 2))
			if bits / len(picture) % 2 != 0 {
				intermediate := combineTo36s(picture)
				picture = split36(intermediate)
			}
			picture = enhance4(picture, rules4)
			size = (size / 2) * 3
		} else {
			picture = enhance9(picture, rules9)
			size = (size / 3) * 4
		}
	}

	return picture
}

func combineTo36s(picture []uint) []uint {
	bits := len(picture) * 9
	size := int(math.Sqrt(float64(bits)))
	intermedLength := bits / 36
	intermediate := make([]uint, intermedLength)
	x := 2 + ((size - 6) / 3)
	starts := []int{0, 1, x, x + 1}
	rows := int(math.Sqrt(float64(intermedLength)))

	for i := 0; i < intermedLength; i++ {
		new36 := uint(0)

		for idx, picIdx := range starts {
			currBits := picture[picIdx]
			if idx == 0 {
				new36 |= (currBits << 27) & 60129542144
				new36 |= (currBits << 24) & 939524096
				new36 |= (currBits << 21) & 14680064
			}
			if idx == 1 {
				new36 |= (currBits << 24) & 7516192768
				new36 |= (currBits << 21) & 117440512
				new36 |= (currBits << 18) & 1835008
			}
			if idx == 2 {
				new36 |= (currBits << 9) & 229376
				new36 |= (currBits << 6) & 3584
				new36 |= (currBits << 3) & 56
			}
			if idx == 3 {
				new36 |= (currBits << 6) & 28672
				new36 |= (currBits << 3) & 448
				new36 |= (currBits) & 7
			}
			

			if (i + 1) % rows == 0 && i != 0 {
				starts[idx] += x
			}
			starts[idx] += 2
		}
		intermediate[i] = new36
	}
	return intermediate
}

func split36(bits36 []uint) []uint {
	var out []uint

	for _, bits := range bits36 {
		out = append(out, []uint{((bits >> 32) &12) | ((bits >> 28) &3),
		((bits >> 30) &12) | ((bits >> 26) &3),
		((bits >> 28) &12) | ((bits >> 24) &3),
		((bits >> 20) &12) | ((bits >> 16) &3),
		((bits >> 18) &12) | ((bits >> 14) &3),
		((bits >> 16) &12) | ((bits >> 12) &3),
		((bits >> 8) &12) | ((bits >> 4) &3),
		((bits >> 6) &12) | ((bits >> 2) &3),
		((bits >> 4) &12) | ((bits) &3),
	}...
	)
	}
	return out
}

func enhance4(picture []uint, rules4 map[uint]uint) []uint {
	out := []uint{}

	for _, square := range picture {
 		for i := 0; true; i++ {
			_, exists:= rules4[square]
			if exists {break}
			if i % 3 == 0 {
				square = flipVert4(square)
			} else if i % 3 == 1 {
				square = flipVert4(square)
			} else {
				square = rotate4(square)
			}
		}
		newSquare, _ := rules4[square]
		out = append(out, newSquare)
	}

	return out
}

func enhance9(picture []uint, rules9 map[uint]uint) []uint {
	out := []uint{}

	for _, square := range picture {
		for i := 0; true; i++ {
			_, exists:= rules9[square]
			if exists {break}
			if i % 3 == 0 {
				square = flipVert9(square)
			} else if i % 3 == 1 {
				square = flipVert9(square)
			} else {
				square = rotate9(square)
			}
		}
		newSquare, _ := rules9[square]
		splitSquare := split4by4(newSquare)
		out = append(out, splitSquare...)
	}

	return out
}

func split4by4(bits16 uint) []uint {
	one := ((bits16 & 49152) >> 12) | ((bits16 & 3072) >> 10)
	two := ((bits16 & 12288) >> 10) | ((bits16 & 768) >> 8)
	three := ((bits16 & 192) >> 4) | ((bits16 & 12) >> 2)
	four := ((bits16 & 48) >> 2) | (bits16 & 3)
	out := []uint{one, two, three, four}
	return out
}

func flipVert4(bits4 uint) uint {
	return ((bits4 << 2) & 12) | (bits4 >> 2)
}

func flipDiag4(bits4 uint) uint {
	midBits := bits4 & 6
	out := midBits | (bits4 >> 3) | ((bits4 << 3) & 8)
	return out
}

func flipVert9(bits9 uint) uint {
	return ((bits9 << 6) & 448) | (bits9 & 56) | (bits9 >> 6)
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