from typing import TextIO

def main():
    grid: list[list[int]] = parse("2015/day_18/input.txt")
    for _ in range(100):
        grid = step_lights(grid)
    print(len([light for row in grid for light in row if light]))
    grid = parse("2015/day_18/input.txt")
    for position in [(0,0), (0,99), (99,0), (99,99)]:
        col, row = position
        grid[row][col] = 1
    for _ in range(100):
        grid = step_lights(grid, False)
    print(len([light for row in grid for light in row if light]))

def parse(input_file: str) -> list[list[int]]:
    in_file: TextIO
    with open(input_file, "r", encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    split_lines: list[str] = input_data.split("\n")
    grid: list[list[int]] = [[0 if light == "." else 1 for light in line] for line in split_lines]
    return grid


def step_lights(grid: list[list[int]], part_1=True):
    new_grid = [[0] * 100 for _ in range(100)]
    for row_num, row in enumerate(grid):
        for col_num, light in enumerate(row):
            position: complex = complex(col_num, row_num)
            if not part_1:
                new_grid[row_num][col_num] = part_2(light, position, grid)
            count_on: int = check_neighbors(position, grid)
            if light:
                if count_on in (2, 3):
                    new_grid[row_num][col_num] = 1
            else:
                if count_on == 3:
                    new_grid[row_num][col_num] = 1
    return new_grid

def part_2(light, position, grid):
    if position in (
        0j,
        99 * 1j,
        99 + 0j,
        99 + 99 * 1j,
    ):
        return 1

    count_on: int = check_neighbors(position, grid)
    if light:
        if count_on in (2, 3):
            return 1
    if count_on == 3:
        return 1
    return 0


def check_neighbors(position: complex, grid: list[list[int]]) -> int:
    count_on: int = 0
    neighbors: list[complex] = [1j, 1 + 1j, 1, 1 - 1j, -1j, -1 - 1j, -1, -1 + 1j]
    for neighbor_pos in map(lambda neighbor: position + neighbor, neighbors):
        row_num: int = int(neighbor_pos.imag)
        col_num: int = int(neighbor_pos.real)
        if row_num < 0 or col_num < 0 or len(grid) == row_num or len(grid[0]) == col_num:
            continue
        neighbor: int = grid[row_num][col_num]
        if neighbor:
            count_on += 1
    return count_on



if __name__ == "__main__":
    main()