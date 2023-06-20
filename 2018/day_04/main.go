package main

import (
	"fmt"
	"regexp"
	. "strings"
	. "time"

	. "github.com/alecswift/advent_of_code/stringOps"
	"github.com/alecswift/advent_of_code/util"
)

type Event struct {
	eTime  Time
	event string
}

func main() {
	events := parse("/home/alec/Desktop/code/advent-of-code/2018/day_04/input.txt")
	sortEvents(events)
	fmt.Print(events)
	// make hash map of gaurds
	// total time
	//array for each minute
}

func buildGuardMap(events []Event) map[int][60]int {
	var currGuard int
	var start, end int
	guardMap := make(map[int][60]int)

	for _, event := range events {
		switch event.event[:5] {
		case "Guard":
			guardNum := parseGuardNum(event.event)
			addToDict(guardNum, guardMap)
			currGuard = guardNum
		case "falls":
			start = event.eTime.Minute()
		case "wakes":
			end = event.eTime.Minute()
			addTimes(guardMap, currGuard, start, end)
		}
	}
	
	return guardMap
}

func addTimes(guardMap map[int][60]int, guard, start, end int) {
	for i := start; i < end; i++ {
		arr := guardMap[guard]
		arr[i]++
	}
}

func addToDict(num int, dict map[int][60]int) {
	_, exists := dict[num]
	if !exists {
		dict[num] = [60]int{}
	}
}

func parseGuardNum(event string) int {
	re := regexp.MustCompile(`\d+`)
	numStr := re.FindAllString(event, -1)
	return StrToInt(numStr[0])
}

func sortEvents(events []Event) {
	for i := 1; i < len(events); i++ {
		event := events[i]
		time := event.eTime
		j := i - 1

		for ; j >= 0 && time.Before(events[j].eTime); j-- {
			events[j + 1] = events[j]
		}
		events[j + 1] = event
	}
}

func parse(inputFile string) []Event {
	data := util.FileToStr(inputFile)
	splitLines := Split(data, "\n")
	events := []Event{}

	for _, line := range splitLines {
		data := Split(line, "] ")
		rawTime, eventStr := data[0][1:], data[1]
		year, month := StrToInt(rawTime[:4]), StrToInt(rawTime[5:7])
		sday, shr, smin := rawTime[8:10], rawTime[11:13], rawTime[14:]
		day, hr, min := StrToInt(sday), StrToInt(shr), StrToInt(smin)

		eTime := Date(year, Month(month), day, hr, min, 0, 0, UTC)
		event := Event{
			eTime: eTime,
			event: eventStr,
		}
		events = append(events, event)
	}

	return events
} 