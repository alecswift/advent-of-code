"""Puzzle explanation: https://adventofcode.com/2016/day/24"""

import heapq
from line_profiler import LineProfiler

def main():
    unvisited, goals = parse("2016/day_24/input.txt")
    distance = dijsktras(goals["7"], goals["1"], unvisited)
    print(distance)


    """lp = LineProfiler()
    lp_wrapper = lp(dijsktras)
    lp_wrapper(goals["0"], goals["3"], unvisited)
    lp.print_stats()"""
    

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
    unvisited = set()
    for col_num, val in enumerate(grid[1]):
        path_down = grid[2][col_num] != "#"
        if val == "#":
            left_node = None
        elif path_down:
            new_node = Node((1, col_num), val)
            if left_node is not None:
                left_row_num, left_col_num = left_node.pos
                left_node.neighbors.append(new_node)
                new_node.neighbors.append(left_node)
            left_node = new_node
            nodes_up[col_num] = new_node
            unvisited.add(new_node)
    
    goals = {}
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
                
                if val.isdigit():
                    goals[val] = new_node
                unvisited.add(new_node)

    return unvisited, goals

def dijsktras(start, target, unvisited):
    queue = [(0, 0, start)]
    entry = 1

    dists = {node: float("inf") for node in unvisited}
    dists[start] = 0
    visited = set()

    while queue[0][2] != target:
        curr_dist, _, curr_node = queue[0]
        heapq.heappop(queue)

        curr_pos = curr_node.pos
        for neighbor in curr_node.neighbors:
            if neighbor in visited:
                continue

            dist = curr_dist + distance(curr_pos, neighbor.pos)
            if dist < dists[neighbor]:
                dists[neighbor] = dist
            
            heapq.heappush(queue, (dist, entry, neighbor))
            entry += 1

        
        visited.add(curr_node)
    
    return dists[target]


def distance(start_pos, end_pos):
    x_coord, y_coord = start_pos
    x_coord_2, y_coord_2 = end_pos
    return abs(x_coord - x_coord_2) + abs(y_coord - y_coord_2)


if __name__ == "__main__":
    main()