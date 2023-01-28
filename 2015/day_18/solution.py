from typing import TextIO

def main():
    grid = parse("2015/day_18/input.txt")
    for _ in range(100):
        grid = step_lights(grid)
    print(len([light for row in grid for light in row if light]))

def parse(input_file: str) -> list[list[int]]:
    in_file: TextIO
    with open(input_file, "r", encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    split_lines: list[str] = input_data.split("\n")
    grid: list[list[int]] = [[0 if light == "." else 1 for light in line] for line in split_lines]
    return grid


def step_lights(grid: list[list[int]]):
    new_grid = [[0] * 100 for _ in range(100)]
    for row_num, row in enumerate(grid):
        for col_num, light in enumerate(row):
            count_on = check_neighbors(complex(col_num, row_num), grid)
            if light:
                if count_on in (2, 3):
                    new_grid[row_num][col_num] = 1
            else:
                if count_on == 3:
                    new_grid[row_num][col_num] = 1
    return new_grid


def check_neighbors(position: complex, grid: list[list[int]]) -> int:
    count_on: int = 0
    neighbors: list[complex] = [1j, 1 + 1j, 1, 1 - 1j, -1j, -1 - 1j, -1, -1 + 1j]
    for neighbor_pos in map(lambda neighbor: position + neighbor, neighbors):
        row_num = int(neighbor_pos.imag)
        col_num = int(neighbor_pos.real)
        if row_num < 0 or col_num < 0 or len(grid) == row_num or len(grid[0]) == col_num:
            continue
        neighbor = grid[row_num][col_num]
        if neighbor:
            count_on += 1
    return count_on



if __name__ == "__main__":
    main()