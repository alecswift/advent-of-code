"""Puzzle explanation: https://adventofcode.com/2015/day/9"""

from collections import deque
from re import findall, split


def main():
    indices, connections = parse("2015/day_9/input.txt")
    short_distances = []
    long_distances = []
    for node in indices:
        min_distance, max_distance = bfsearch(node, connections, indices)
        short_distances.append(min_distance)
        long_distances.append(max_distance)
    print(f'The shortest route santa can take is {min(short_distances)}')
    print(f'The longest route santa can take is {max(long_distances)}')


def parse(input_file):
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    nodes = set()
    connections = {}
    for line in split('\n', input_data):
        node, neighbor, weight = findall(r"(.+) to (.+) = (\d+)", line)[0]
        nodes.add(neighbor)
        nodes.add(node)
        if node not in connections:
            connections[node] = [(neighbor, int(weight))]
        else:
            connections[node].append((neighbor, int(weight)))
        if neighbor not in connections:
            connections[neighbor] = [(node, int(weight))]
        else:
            connections[neighbor].append((node, int(weight)))
    return dict(zip(nodes, range(0, len(nodes)))), connections

def bfsearch(start_node, connections, indices):
    """
    Searches all possible paths from the start node that visit
    each node exactly once
    """
    distances = []
    queue = deque()
    queue.append((start_node, 0, 0)) # current node, distance, bitmask
    while queue:
        current_node, distance, bitmask = queue[0]
        bit = 1 << indices[current_node]
        bitmask = bitmask | bit # the set of nodes that are visited
        if bitmask == 2**len(indices) - 1: # if all nodes are visited
            distances.append(distance)
        for neighbor, weight in connections[current_node]:
            neighbor_bit = 1 << indices[neighbor]
            if not bitmask & neighbor_bit: # if the neighbor has not been visited
                queue.append((neighbor, distance + weight, bitmask))
        queue.popleft()
    return min(distances), max(distances)

if __name__ == "__main__":
    main()
