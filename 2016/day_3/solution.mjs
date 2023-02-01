
import { readFileSync } from "fs";

const triangles = readFileSync('2016/day_3/input.txt', 'utf8').split("\n")

function findTriangles(triangles) {
    let triangleCount = 0
    for (let triangle of triangles) {
        let arrTriangle = triangle.split(/\s+/)
        arrTriangle.shift()
        for (let i = 0; i < 3; i ++) {
            arrTriangle[i] = parseInt(arrTriangle[i])
        }
        let [A, B, C] = arrTriangle
        const isValidTriangle = (A + B > C) && (B + C > A) && (A + C > B)
        if (isValidTriangle) {
            triangleCount ++
        }
    }
    return triangleCount;
}

console.log(findTriangles(triangles))