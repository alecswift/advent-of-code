// Puzzle explanation: https://adventofcode.com/2016/day/2

import { readFileSync } from 'fs';

const instructions = readFileSync('2016/day_02/input.txt', 'utf8').replaceAll("\n", "C")
const keyPad1 = [
    [null, null, null, null],
    [null, '1', '2', '3', null],
    [null, '4', '5', '6', null],
    [null, '7', '8', '9', null],
    [null, null, null, null] 
]
const keyPad2 = [
    [null, null, null, null, null, null, null],
    [null, null, null, '1', null, null, null],
    [null, null, '2', '3', '4', null, null],
    [null, '5', '6', '7', '8', '9', null],
    [null, null, 'A', 'B', 'C', null, null],
    [null, null, null, 'D', null, null, null],
    [null, null, null, null, null, null, null]
];

function solution(instructions, part1) {
    // Defines variables that initialize differently for part 1 and part 2
    if (part1) {
        var keyPad = keyPad1
        var row = 2
        var col = 2
    } else {
        var keyPad = keyPad2
        var row = 3
        var col = 1
    }
    let code = []
    // Move position in matrix depending on the instruction
    for (let instruction of instructions) {
        let temp_row = row
        let temp_col = col
        switch (instruction) {
            // C represents a line break in the instructions here we enter the
            // current position on the keypad into the code array
            case "C":
                code.push(keyPad[row][col])
                break
            case "U":
                temp_row -= 1
                break
            case "D":
                temp_row += 1
                break
            case "R":
                temp_col += 1
                break
            case "L":
                temp_col -= 1
        }
        // If we hit a border (null) keep the original position
        if (keyPad[temp_row][temp_col] === null) {
            continue
        }
        row = temp_row
        col = temp_col
    }
    return code;
}

const part1Sol = solution(instructions, true).join("")
const part2Sol = solution(instructions, false).join("")
console.log(part1Sol, part2Sol);
