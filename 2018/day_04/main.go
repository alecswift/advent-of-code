package main

import (
	"fmt"
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
		day, hr, min := StrToInt(rawTime[:4]), StrToInt(rawTime[:4]), StrToInt(rawTime[:4])
		eTime := Date(year, Month(month), day, hr, min, 0, 0, UTC)
		event := Event{
			eTime: eTime,
			event: eventStr,
		}
		events = append(events, event)
	}

	return events
} 