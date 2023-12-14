// https://adventofcode.com/2023/day/2

package main

import (
	"fmt"
	"regexp"
	"strings"

	"github.com/alecswift/advent_of_code/stringOps"
	"github.com/alecswift/advent_of_code/util"
)

type Hand struct {
	red   int
	green int
	blue  int
}

func main() {
	strData := util.FileToStr("/home/alec/Desktop/code/advent-of-code/2023/day_02/input.txt")
	games := parse(strData)
	maxes := Hand{
		red: 12,
		green: 13,
		blue: 14,
	}
	part1Sol := part1(games, maxes)
	part2Sol := part2(games)
	fmt.Print(part1Sol, " ", part2Sol)
}

func part1(games [][]Hand, maxes Hand) int {
	var impossible bool
	sum := 0

	for idx, game := range games {
		id := idx + 1
		for _, hand := range game {
			impossibleHand := hand.blue > maxes.blue || hand.red > maxes.red || hand.green > maxes.green
			if impossibleHand {
				impossible = true
			}
		}
		if !impossible {
			sum += id
		} else {
			impossible = false
		}
	}

	return sum
}

func part2(games [][]Hand) int {
	sum := 0

	for _, game := range games {
		mins := Hand{
			red: 0,
			green: 0,
			blue: 0,
		}

		for _, hand := range game {
			mins = newMins(mins, hand)
		}
		sum += mins.red * mins.green * mins.blue
	}
	return sum
}

func newMins(mins, hand Hand) Hand {
	if mins.red == 0 || hand.red > mins.red {
		mins.red = hand.red
	}
	if mins.blue == 0 || hand.blue > mins.blue {
		mins.blue = hand.blue
	}
	if mins.green == 0 || hand.green > mins.green {
		mins.green = hand.green
	}
	return mins
}

func parse(data string) [][]Hand {
	lines := strings.Split(data, "\n")
	games := [][]Hand{}

	for idx, line := range lines {
		line = line[8:]
		hands := strings.Split(line, ";")
		games = append(games, []Hand{})

		for _, handStr := range hands {
			hand := makeHandStruct(handStr)
			games[idx] = append(games[idx], hand)
		}
	}

	return games
}

func makeHandStruct(handStr string) Hand {
	var hand Hand

	reBlue := regexp.MustCompile(`\d+ blue`)
	reRed := regexp.MustCompile(`\d+ red`)
	reGreen := regexp.MustCompile(`\d+ green`)
	matchesBlue := reBlue.FindAllString(handStr, -1)
	matchesRed := reRed.FindAllString(handStr, -1)
	matchesGreen := reGreen.FindAllString(handStr, -1)

	if len(matchesBlue) == 0 {
		hand.blue = 0
	} else {
		re := regexp.MustCompile(`\d+`)
		strNum := re.FindAllString(matchesBlue[0], -1)[0]
		num := stringOps.StrToInt(strNum)
		hand.blue = num
	}

	if len(matchesRed) == 0 {
		hand.red = 0
	} else {
		re := regexp.MustCompile(`\d+`)
		strNum := re.FindAllString(matchesRed[0], -1)[0]
		num := stringOps.StrToInt(strNum)
		hand.red = num
	}

	if len(matchesGreen) == 0 {
		hand.green = 0
	} else {
		re := regexp.MustCompile(`\d+`)
		strNum := re.FindAllString(matchesGreen[0], -1)[0]
		num := stringOps.StrToInt(strNum)
		hand.green = num
	}

	return hand
}
