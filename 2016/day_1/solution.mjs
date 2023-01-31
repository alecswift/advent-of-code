// Puzzle Explanation: https://adventofcode.com/2016/day/1

import { complex, add } from 'mathjs'
import { readFileSync } from 'fs';

const instructions = readFileSync('day_1/input.txt', 'utf8').split(", ");

function solution(instructions) {
    let part2 = false
    let position = complex(0,0)
    let part2Pos = null
    // North, South, East, West
    let seen = [position]
    let orientations = [
        complex(0, 1),
        complex(1, 0),
        complex(0, -1),
        complex(-1, 0)
    ]
    for (let instruction of instructions) {
        let direction = instruction[0]
        let spaces = Number(instruction.slice(1, instruction.length))
        switch (direction) {
            case 'L':
                let top = orientations.pop()
                orientations.unshift(top)
                break
            case 'R':
                let bottom = orientations.shift()
                orientations.push(bottom)
        }
        // modify position based on spaces and current orientation
        for (let j = 0; j < spaces; j ++) {
            position = add(position, orientations[0])
            // Find the first coordinate that appears twice
            if (!part2) {
                if (linearSearch(seen, position)) {
                    part2Pos = position
                    part2 = true
                } else {
                    seen.push(position)
                }
            }
        }
    }
    const part1sol = Math.abs(position.re) + Math.abs(position.im)
    const part2sol = Math.abs(part2Pos.re) + Math.abs(part2Pos.im)
    return [part1sol, part2sol]
}

function linearSearch(coords, target) {
    for (let coord of coords) {
        if (coord.equals(target)) {
            return true
        }
    }
    return false
}

console.log(solution(instructions))