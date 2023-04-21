package main

import (
	"reflect"
	"fmt"
	"regexp"
	"strings"

	"github.com/alecswift/advent_of_code/stringOps"
	"github.com/alecswift/advent_of_code/util"
)

func main() {
	instructions := parse("/home/alec/Desktop/code/advent-of-code/2017/day_16/input.txt")
	letters := "abcdefghijklmnop"
	seqPart1 := strings.Split(letters, "")
	part1Sol := part1(seqPart1, instructions)
	fmt.Print(part1Sol, "\n")
	initialSeq := strings.Split(letters, "") 
	seq := strings.Split(letters, "")
	
	part2Seq := part2(seq, initialSeq, instructions)
	part2Sol := strings.Join(part2Seq, "")
	fmt.Print(part2Sol)
	
}

func part1(seq, instructions []string) []string {
	var i int

	for i < len(instructions) {
		switch instructions[i] {
		case "s":
			num := stringOps.StrToInt(instructions[i + 1])
			seq = spin(seq, num)
			i += 2
		case "p":
			seq = partner(seq, instructions[i + 1], instructions[i + 2])
			i += 3
		case "x":
			num1 := stringOps.StrToInt(instructions[i + 1])
			num2 := stringOps.StrToInt(instructions[i + 2])
			seq[num1], seq[num2] = seq[num2], seq[num1]
			i += 3
		}
	}
	return seq
}

func part2(seq, initialSeq, instructions []string) []string {
	cycleNum := 1
	seq = part1(seq, instructions)
	seqs := make(map[int][]string)
	seqs[0] = initialSeq

	for !reflect.DeepEqual(initialSeq, seq) {
		seqs[cycleNum] = seq
		cpySeq := make([]string, len(seq))
		copy(cpySeq, seq)
		seq = part1(cpySeq, instructions)
		cycleNum++
	}

	cycles := len(seqs)
	daOne := 1000000000 % cycles
	return seqs[daOne]
}

func parse(inputFile string) []string {
	inputData := util.FileToStr(inputFile)
	re := regexp.MustCompile(`[a-z]|\d+`)
	instructions := re.FindAllString(inputData, -1)

	return instructions
}

func spin(seq []string, num int) []string {
	split_idx := len(seq) - num
	out := seq[split_idx:]
	out = append(out, seq[:split_idx]...)

	return out
}

func partner(seq []string, char1, char2 string) []string {
	var idx1, idx2 int

	for idx, char := range seq {
		if char == char1 {
			idx1 = idx
		}

		if char == char2 {
			idx2 = idx
		}
	}

	seq[idx1], seq[idx2] = seq[idx2], seq[idx1]
	
	return seq
}
