"""Puzzle explanation: https://adventofcode.com/2016/day/24"""

import heapq
from collections import OrderedDict
from line_profiler import LineProfiler

def main():
    unvisited, goals = parse("2016/day_24/input.txt")
    """for num_1 in range(8):
        for num_2 in range(num_1 + 1, 8):
            distance = dijsktras(goals[str(num_1)], goals[str(num_2)], unvisited)
            print(num_1, " ", num_2, " ", distance)
    print(distance)"""
    #distance = dijsktras(goals["4"], goals["0"], unvisited)
    #print(distance)
    nodes = OrderedDict({
        0 : {1: 20, 2: 76, 3: 28, 4: 238, 5: 220, 6: 16, 7: 166},
        1 : {0: 20, 2: 76, 3: 44, 4: 234, 5: 216, 6: 24, 7: 162},
        2 : {0: 76, 1: 76, 3: 92, 4: 302, 5: 284, 6: 88, 7: 230},
        3 : {0: 28, 1: 44, 2: 92, 4: 230, 5: 212, 6: 32, 7: 162},
        4 : {0: 238, 1: 234, 2: 302, 3: 230, 5: 38, 6: 230, 7: 84},
        5 : {0: 220, 1: 216, 2: 284, 3: 212, 4: 38, 6: 212, 7: 66},
        6 : {0: 16, 1: 24, 2: 88, 3: 32, 4: 230, 5: 212, 7: 162},
        7 : {0: 166, 1: 162, 2: 230, 3: 162, 4: 84, 5: 66, 6: 162}
    })
    
    minimum = dfs(0, nodes)
    print(minimum)

    """lp = LineProfiler()
    lp_wrapper = lp(dijsktras)
    lp_wrapper(goals["0"], goals["3"], unvisited)
    lp.print_stats()"""
    

class Node:

    def __init__(self, pos, val):
        self.pos = pos
        self.val = val
        self.neighbors = set()
        self.goal_dists = {}

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
                dist = distance((1, col_num), left_node.pos)
                left_node.neighbors.add((new_node, dist))
                new_node.neighbors.add((left_node, dist))
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
                    dist = distance((row_num, col_num), left_node.pos)
                    left_node.neighbors.add((new_node, dist))
                    new_node.neighbors.add((left_node, dist))
                if path_up:
                    dist = distance((row_num, col_num), up_node.pos)
                    up_node.neighbors.add((new_node, dist))
                    new_node.neighbors.add((up_node, dist))
                left_node = new_node
                nodes_up[col_num] = new_node
                
                if val.isdigit():
                    goals[val] = new_node
                unvisited.add(new_node)

    # prune deadends
    deadends = []
    for node in unvisited:
        if len(node.neighbors) == 1:
            deadends.append(node)

    while deadends:
        curr_node = deadends[0]
        while not curr_node.val.isdigit() and len(curr_node.neighbors) == 1:
            unvisited.remove(curr_node)
            neighbor, dist = next(iter(curr_node.neighbors))
            neighbor.neighbors.remove((curr_node, dist))
            curr_node = neighbor
        deadends.pop(0)

    # add to nodes manhattan distance to goals for a* heuristic
    for node in unvisited:
        for val, goal_node in goals.items():
            node.goal_dists[val] = distance(node.pos, goal_node.pos)

    return unvisited, goals

def dijsktras(start, target, unvisited):
    queue = [(0, 0, 0, start)]
    entry = 1

    dists = {node: float("inf") for node in unvisited}
    dists[start] = 0
    visited = set()

    while queue[0][3] != target:
        weight, _, curr_dist, curr_node = queue[0]
        # if curr_dist > 170:
            # break
        heapq.heappop(queue)

        for neighbor, dist in curr_node.neighbors:
            if neighbor in visited:
                continue

            new_dist = curr_dist + dist
            if new_dist < dists[neighbor]:
                dists[neighbor] = new_dist
            
            new_weight = new_dist + neighbor.goal_dists[target.val]
            heapq.heappush(queue, (new_weight, entry, new_dist, neighbor))
            entry += 1

        
        visited.add(curr_node)
    
    return dists[target]

def dfs(curr_node, nodes, bitmask=1, full_dist = 0, mins = None, prev=None):
    if mins is None:
        mins = []
    if bitmask == 2**len(nodes) - 1:
        mins.append(full_dist + nodes[prev][0])
        return
    for neighbor, dist in nodes[curr_node].items():
        bit = 1 << neighbor
        if bitmask & bit:
            continue
        dfs(neighbor, nodes, bitmask | bit, full_dist + dist, mins, neighbor) 
    return min(mins)


def distance(start_pos, end_pos):
    x_coord, y_coord = start_pos
    x_coord_2, y_coord_2 = end_pos
    return abs(x_coord - x_coord_2) + abs(y_coord - y_coord_2)


if __name__ == "__main__":
    main()