// Puzzle Explanation: https://adventofcode.com/2016/day/3

import { readFileSync } from "fs";

const triangles = readFileSync('day_3/input.txt', 'utf8').split("\n")
let triangle1 = []
let triangle2 = []
let triangle3 = []
let trianglesPart2 = [triangle1, triangle2, triangle3]

function findTriangles(triangles) {
    // Iterates over triangle data and tests if the triangles are valid
    let triangleCount = 0
    let triangleCount2 = 0
    let idx = 0
    for (let triangle of triangles) {
        let arrTriangle = triangle.split(/\s+/)
        arrTriangle.shift()
        for (let i = 0; i < 3; i ++) {
            arrTriangle[i] = parseInt(arrTriangle[i])
        }
        if (isValidTriangle(arrTriangle)) {
            triangleCount ++
        }
        triangleCount2 += part2(arrTriangle, idx)
        idx ++
    }
    return [triangleCount, triangleCount2];
}

function part2(arrTriangle, idx) {
    // Tests triangles validity when we have three triangles defined
    // after every 3 indices (due to triangles being located in columns)
    let triangleCount2 = 0
    for (let i = 0; i < 3; i ++) {
        trianglesPart2[i].push(arrTriangle[i])
    }
    if ((idx + 1) % 3 === 0) {
        for (let i = 0; i < 3; i ++) {
            if (isValidTriangle(trianglesPart2[i])) {
                triangleCount2 ++
            }
            trianglesPart2[i] = []
        }
    }
    return triangleCount2
}

function isValidTriangle(arrTriangle) {
    let [A, B, C] = arrTriangle
    const isValid = (A + B > C) && (B + C > A) && (A + C > B)
    return (isValid);
}

let [part1Solution, part2Solution] = findTriangles(triangles)
console.log(part1Solution, part2Solution)
