"""Puzzle explanation: https://adventofcode.com/2016/day/13"""

from collections import deque

def main():
    TARGET = complex(31, 39)
    ADDER = 1352
    steps, locations_under_50 = bfs(TARGET, ADDER)
    print(steps)
    print(locations_under_50)

def is_wall(coord: complex, adder) -> bool:
    x_coord, y_coord = int(coord.real), int(coord.imag)
    new = (x_coord**2) + (3*x_coord) + (2 * x_coord * y_coord) + y_coord + (y_coord**2)
    new += adder
    count_1_bit = sum(1 for bit in bin(new) if bit == '1')
    return count_1_bit % 2 == 1

def bfs(target: complex, adder: int) -> tuple[int, int]:
    seen = set()
    start = complex(1, 1), 0
    queue = deque([start])
    directions = [1j, 1+0j,-1+0j,-1j]
    locations_under_50: set[complex] = set()
    while True:
        coord, steps = queue[0]
        if coord == target:
            return steps, len(locations_under_50)
        if queue[0] in seen:
            queue.popleft()
            continue
        if is_wall(coord, adder):
            queue.popleft()
            continue
        if coord.real < 0 or coord.imag < 0:
            queue.popleft()
            continue
        for direction in directions:
            neighbor = coord + direction
            queue.append((neighbor, steps + 1))
        seen.add(queue[0])
        if steps <= 50:
            locations_under_50.add(coord)
        queue.popleft()

if __name__ == "__main__":
    main()
