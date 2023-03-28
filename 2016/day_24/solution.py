"""Puzzle explanation: https://adventofcode.com/2016/day/24"""

from collections import deque

def main():
    start = parse("2016/day_24/input_test.txt")
    x = 1
    

class Node:

    def __init__(self, pos, val):
        self.pos = pos
        self.val = val
        self.neighbors = []

def parse(input_file):
    with open(input_file, "r", encoding = "utf-8") as in_file:
        input_data = in_file.read()
    grid = input_data.split("\n")
    nodes_up = [None] * len(grid[0])
    left_node = None
    for col_num, val in enumerate(grid[1]):
        path_down = grid[2][col_num] != "#"
        if val == "#":
            left_node = None
        elif path_down:
            new_node = Node((1, col_num), val)
            if left_node is not None:
                left_node.neighbors.append(new_node)
                new_node.neighbors.append(left_node)
            left_node = new_node
            nodes_up[col_num] = new_node
    
    start = None
    for idx, row in enumerate(grid[2:-1]):
        left_node = None
        row_num = idx + 2
        for idx2, val in enumerate(row[1:-1]):
            col_num = idx2 + 1
            if val == "#":
                left_node = None
                nodes_up[col_num] = None
                continue

            up_node = nodes_up[col_num]
            # these next two statements and in the previous
            # loop need to check
            path_right = grid[row_num][col_num + 1] != "#"
            path_down = grid[row_num + 1][col_num] != "#"
            path_up = up_node is not None
            path_left = left_node is not None
            junction = not (
                (path_left and path_right and not path_down and not path_up) or
                (path_up and path_down and not path_left and not path_right)
            )
            if val.isdigit() or junction:
                new_node = Node((row_num, col_num), val)
                if path_left:
                    left_node.neighbors.append(new_node)
                    new_node.neighbors.append(left_node)
                if path_up:
                    nodes_up[col_num].neighbors.append(new_node)
                    new_node.neighbors.append(nodes_up[col_num])
                left_node = new_node
                nodes_up[col_num] = new_node
                
                if val == "0":
                    start = new_node

    return start

            



    # need to optimize pathfinding here with cutting down number of nodes
    # add distance as weights between nodes and use 
    # use dijsktras algorithm
                
            
def bfs(start, grid, target):
    queue = deque([(start, 0)])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()
    while queue:
        curr_pos, steps = queue[0]
        visited.add(curr_pos)
        if 180 < steps:
            return -1
        curr_row, curr_col = curr_pos
        for direction in directions:
            neighbor_row, neighbor_col = curr_row + direction[0], curr_col + direction[1]
            neighbor = (neighbor_row, neighbor_col)
            if neighbor == target:
                return steps + 1
            if grid[neighbor_row][neighbor_col] == "#" or neighbor in visited:
                continue
            queue.append((neighbor, steps + 1))
        queue.popleft()


if __name__ == "__main__":
    main()