// Puzzle Explanation: https://adventofcode.com/2016/day/1

import { readFileSync } from 'fs';

const instructions = readFileSync('day_1/input.txt', 'utf8').split(", ");

function solution(instructions) {
    let position = [0, 0]
    // North, South, East, West
    let orientations = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]
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
        for (let i = 0; i < position.length; i ++) {
            if (orientations[0][i] !== 0) {
                position[i] += (orientations[0][i] * spaces)
            }
        }
    }
    return Math.abs(position[0]) + Math.abs(position[1])
}

console.log(solution(instructions))