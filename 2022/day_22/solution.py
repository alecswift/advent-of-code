"""
Find the final position after following the given directions
from the start point
"""
from collections import deque
from itertools import zip_longest
from re import findall
from numpy import array


def initial_parse(input_file):
    """
    Return the parsed grid and procedure from the given input file
    """
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    grid_str, procedure_str = input_data.split("\n\n")
    procedure = [
        int(instruction) if instruction.isdigit() else instruction
        for instruction in findall(r"[\d]+|[RL]", procedure_str)
    ]
    grid = grid_str.split("\n")
    return grid, procedure


def parse(grid):
    "Return the rows and columns of a given grid"
    rows = [list(row) for row in grid]
    max_x = max([len(row) for row in rows])
    # Add white spaces to the end of rows to equalize lengths
    for row in rows:
        length = len(row)
        if length < max_x:
            row.extend([" "] * (max_x - length))
    columns = array(rows).transpose().tolist()
    return rows, columns


def wrapper(rows):
    """
    Return a hash map of the points that wrap around to eachother on the
    rows of the grid. Additionally, return the wall coordinates and the
    start point at the top left nonempty corner of the grid.
    """
    walls = set()
    west_wrappers = {}
    east_wrappers = {}
    # While iterating through characters in grid: add wall coordinates to a set
    # and hash the start of nonempty spaces to the end in a wrapper dict
    for y_coord, row in zip(range(len(rows) - 1, -1, -1), rows):
        coords = []
        for x_coord, char in enumerate(row):
            if char != " ":
                coords.append(complex(x_coord, y_coord))
            if char == "#":
                walls.add(complex(x_coord, y_coord))
        west_wrappers[coords[0]] = coords[-1]
        east_wrappers[coords[-1]] = coords[0]

    for key in west_wrappers:
        start_point = key
        break
    return west_wrappers, east_wrappers, walls, start_point


def wrapper_col(columns):
    """
    Return a hash map of the points that wrap around to eachother on the
    columns of the grid
    """
    north_wrappers = {}
    south_wrappers = {}
    # Same as previous function except for columns
    for x_coord, column in enumerate(columns):
        coords = []
        for y_coord, char in zip(range(len(column) - 1, -1, -1), column):
            if char != " ":
                coords.append(complex(x_coord, y_coord))
        north_wrappers[coords[0]] = coords[-1]
        south_wrappers[coords[-1]] = coords[0]
    return north_wrappers, south_wrappers


def execute_proc(start_point, walls, wrappers, procedure):
    """
    Execute the procedure from the start point to find the final point and facing
    for the grid map
    """
    north_wrappers, south_wrappers, west_wrappers, east_wrappers = wrappers
    directions = deque([1, -1j, -1, 1j])
    prev_point = None
    current_point = start_point
    for item in procedure:
        if isinstance(item, int):
            for _ in range(item):
                if current_point in walls:
                    current_point = prev_point
                    break
                if (directions[0] == 1) and (current_point in east_wrappers):
                    prev_point = current_point
                    current_point = east_wrappers[current_point]
                elif (directions[0] == -1) and (current_point in west_wrappers):
                    prev_point = current_point
                    current_point = west_wrappers[current_point]
                elif (directions[0] == 1j) and (current_point in north_wrappers):
                    prev_point = current_point
                    current_point = north_wrappers[current_point]
                elif (directions[0] == -1j) and (current_point in south_wrappers):
                    prev_point = current_point
                    current_point = south_wrappers[current_point]
                else:
                    prev_point = current_point
                    current_point += directions[0]
                    if current_point in walls:
                        current_point = prev_point
        else:
            if item == "L":
                directions.rotate()
            else:
                directions.rotate(-1)
    return current_point, directions[0]


def find_password(input_file):
    """
    Return the password from formula involving the final point and facing
    for the grid map
    """
    grid, procedure = initial_parse(input_file)
    rows, columns = parse(grid)
    west_wrappers, east_wrappers, walls, start_point = wrapper(rows)
    north_wrappers, south_wrappers = wrapper_col(columns)
    wrappers = north_wrappers, south_wrappers, west_wrappers, east_wrappers
    final_coord, facing = execute_proc(start_point, walls, wrappers, procedure)
    facing_scores = {1: 0, -1j: 1, -1: 2, 1j: 3}
    facing_score = facing_scores[facing]
    column_num = final_coord.real + 1
    row_num = len(rows) - final_coord.imag
    return int(1000 * row_num + 4 * column_num + facing_score)


print(find_password("2022/day_22/input.txt"))


def parse_cube(input_file):
    """
    Return a list of matrices of the cube faces, the procedure, the
    start point, and a set of wall coordinates from the input file
    """
    grid, procedure = initial_parse(input_file)
    walls = set(
        complex(x_coord, y_coord)
        for y_coord, row in enumerate(grid)
        for x_coord, char in enumerate(row)
        if char == "#"
    )
    remove_empty = [
        [complex(x_coord, y_coord) for x_coord, char in enumerate(row) if char != " "]
        for y_coord, row in enumerate(grid)
    ]
    edge_length = min([len(row) for row in remove_empty])
    cube_faces = [[] for _ in range(6)]
    current_face = 0
    prev_length = len(remove_empty[0])

    for row in remove_empty:
        length = len(row)
        if length != prev_length:
            current_face += partition
        if length == edge_length:
            partition = 1
            cube_faces[current_face].append(row)
        else:
            partition = length // edge_length
            for num in range(partition):
                cube_faces[current_face + num].append(
                    row[num * edge_length : (num + 1) * edge_length]
                )
        prev_length = length

    start_point = cube_faces[0][0][0]
    return cube_faces, procedure, start_point, walls


def cube_wrappers(cube_faces):
    """
    Return a hash map of the points that wrap around to eachother on the
    on the cube.
    """
    north_wrappers, south_wrappers, east_wrappers, west_wrappers = {}, {}, {}, {}
    cube_face_cols = [array(cube_face).transpose().tolist() for cube_face in cube_faces]
    # dictionary update indices change based on input
    north_wrappers.update(
        zip(cube_faces[0][0], zip_longest(cube_face_cols[5][0], [1], fillvalue=1))
    )
    north_wrappers.update(
        zip(cube_faces[1][0], zip_longest(cube_faces[5][-1], [-1j], fillvalue=-1j))
    )
    north_wrappers.update(
        zip(cube_faces[3][0], zip_longest(cube_face_cols[2][0], [1], fillvalue=1))
    )
    south_wrappers.update(
        zip(cube_faces[1][-1], zip_longest(cube_face_cols[2][-1], [-1], fillvalue=-1))
    )
    south_wrappers.update(
        zip(cube_faces[4][-1], zip_longest(cube_face_cols[5][-1], [-1], fillvalue=-1))
    )
    south_wrappers.update(
        zip(cube_faces[5][-1], zip_longest(cube_faces[1][0], [1j], fillvalue=1j))
    )
    east_wrappers.update(
        zip(
            cube_face_cols[1][-1][::-1],
            zip_longest(cube_face_cols[4][-1], [-1], fillvalue=-1),
        )
    )
    east_wrappers.update(
        zip(cube_face_cols[2][-1], zip_longest(cube_faces[1][-1], [-1j], fillvalue=-1j))
    )
    east_wrappers.update(
        zip(
            cube_face_cols[4][-1][::-1],
            zip_longest(cube_face_cols[1][-1], [-1], fillvalue=-1),
        )
    )
    east_wrappers.update(
        zip(cube_face_cols[5][-1], zip_longest(cube_faces[4][-1], [-1j], fillvalue=-1j))
    )
    west_wrappers.update(
        zip(cube_face_cols[5][0], zip_longest(cube_faces[0][0], [1j], fillvalue=1j))
    )
    west_wrappers.update(
        zip(
            cube_face_cols[3][0][::-1],
            zip_longest(cube_face_cols[0][0], [1], fillvalue=1),
        )
    )
    west_wrappers.update(
        zip(cube_face_cols[2][0], zip_longest(cube_faces[3][0], [1j], fillvalue=1j))
    )
    west_wrappers.update(
        zip(
            cube_face_cols[0][0][::-1],
            zip_longest(cube_face_cols[3][0], [1], fillvalue=1),
        )
    )
    return north_wrappers, south_wrappers, east_wrappers, west_wrappers


def execute_proc_cube(start_point, walls, wrappers, procedure):
    """
    Execute the procedure from the start point to find the final point and facing
    for the cube map
    """
    north_wrappers, south_wrappers, east_wrappers, west_wrappers = wrappers
    directions = deque([1, 1j, -1, -1j])
    current_point = start_point

    for item in procedure:
        if isinstance(item, int):
            for _ in range(item):
                if (directions[0] == 1) and (current_point in east_wrappers):
                    if east_wrappers[current_point][0] not in walls:
                        while directions[0] != east_wrappers[current_point][1]:
                            directions.rotate()
                        current_point = east_wrappers[current_point][0]
                elif (directions[0] == -1) and (current_point in west_wrappers):
                    if west_wrappers[current_point][0] not in walls:
                        while directions[0] != west_wrappers[current_point][1]:
                            directions.rotate()
                        current_point = west_wrappers[current_point][0]
                elif (directions[0] == -1j) and (current_point in north_wrappers):
                    if north_wrappers[current_point][0] not in walls:
                        while directions[0] != north_wrappers[current_point][1]:
                            directions.rotate()
                        current_point = north_wrappers[current_point][0]
                elif (directions[0] == 1j) and (current_point in south_wrappers):
                    if south_wrappers[current_point][0] not in walls:
                        while directions[0] != south_wrappers[current_point][1]:
                            directions.rotate()
                        current_point = south_wrappers[current_point][0]
                elif current_point + directions[0] not in walls:
                    current_point += directions[0]
                else:
                    break
        else:
            if item == "L":
                directions.rotate()
            else:
                directions.rotate(-1)

    return current_point, directions[0]


def find_password_2(input_file):
    """
    Return the password from formula involving the final point and facing
    for the cube map
    """
    cube_faces_1, proc_1, start_point_1, walls_1 = parse_cube(input_file)
    (
        north_wrappers_1,
        south_wrappers_1,
        east_wrappers_1,
        west_wrappers_1,
    ) = cube_wrappers(cube_faces_1)
    wrappers_1 = north_wrappers_1, south_wrappers_1, east_wrappers_1, west_wrappers_1
    end_point, facing = execute_proc_cube(start_point_1, walls_1, wrappers_1, proc_1)
    facing_scores = {1: 0, 1j: 1, -1: 2, -1j: 3}
    password = (
        ((end_point.real + 1) * 4)
        + ((end_point.imag + 1) * 1000)
        + facing_scores[facing]
    )
    return int(password)


print(find_password_2("2022/day_22/input.txt"))
