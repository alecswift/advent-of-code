import { readFileSync } from 'fs';
import { row } from 'mathjs';

const instructions = readFileSync('day_2/input.txt', 'utf8').replaceAll("\n", "C")
console.log(instructions)
const keyPad = [
    [null, null, null, null],
    [null, 1, 2, 3, null],
    [null, 4, 5, 6, null],
    [null, 7, 8, 9, null],
    [null, null, null, null] 
];

function solution(instructions) {
    let code = []
    let row = 2
    let col = 2
    for (let instruction of instructions) {
        let temp_row = row
        let temp_col = col
        switch (instruction) {
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
        if (keyPad[temp_row][temp_col] === null) {
            continue
        }
        row = temp_row
        col = temp_col
    }
    return code;
}

console.log(solution(instructions))