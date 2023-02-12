"""Puzzle explanation: https://adventofcode.com/2015/day/9"""

from re import findall, split


def main():
    indices, connections = parse("2015/day_09/input.txt")
    distances = []
    max_distance = 0
    for node in indices:
        dfssearch(node, connections, indices, 0, distances)
        prev = max_distance
        max_distance = max(prev, dfssearch_max_only(node, connections, indices, 0))
    print(f"The shortes route santa can take is {min(distances)}")
    print(f"The longest route santa can take is {max(distances)}")
    print(f"The longest route santa can take is {max_distance}")


def parse(input_file):
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    nodes = set()
    connections = {}
    for line in split("\n", input_data):
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


def dfssearch(current_node, connections, indices, bitmask, distances, distance=None):
    """
    Searches all possible paths from the start node that visit
    each node exactly once
    """
    # current node, distance, bitmask
    if distance is None:
        distance = 0
    bit = 1 << indices[current_node]
    bitmask = bitmask | bit  # the set of nodes that are visited
    for neighbor, weight in connections[current_node]:
        if bitmask == 2 ** len(indices) - 1:  # if all nodes are visited
            distances.append(distance)
            continue
        # print(weight)
        neighbor_bit = 1 << indices[neighbor]
        if not bitmask & neighbor_bit:  # if the neighbor has not been visited
            dfssearch(
                neighbor, connections, indices, bitmask, distances, distance + weight
            )
    return distance


def dfssearch_max_only(current_node, connections, indices, bitmask):
    """
    Searches all possible paths from the start node that visit
    each node exactly once
    """
    # current node, distance, bitmask
    max_distance = 0
    bit = 1 << indices[current_node]
    bitmask = bitmask | bit  # the set of nodes that are visited
    for neighbor, weight in connections[current_node]:
        if bitmask == 2 ** len(indices) - 1:  # if all nodes are visited
            continue
        # print(weight)
        neighbor_bit = 1 << indices[neighbor]
        if not bitmask & neighbor_bit:  # if the neighbor has not been visited
            max_distance = max(
                max_distance,
                dfssearch_max_only(neighbor, connections, indices, bitmask) + weight,
            )
    return max_distance


if __name__ == "__main__":
    main()
