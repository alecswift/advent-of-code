"""
Find the optimal path through a cave with valves
such that valves are opened in the order that
releases the most pressure in 30 minutes
"""

from collections import deque
from re import split, findall


class Valve:
    """
    Represents a valve with a name, flow_rate, and neighbors
    """
    def __init__(self, name, flow_rate, neighbors):
        self.name = name
        self.flow_rate = flow_rate
        self.neighbors = neighbors
        self.visited = False


class CaveGraph:
    """
    Represents a cave with valves as the vertices and edges as the tunnels
    """
    def __init__(self, data):
        self.data = data
        self.valves = {}
        self.parse()
        self.valves_not_zero = {
            name: valve
            for name, valve in self.valves.items()
            if valve.flow_rate or valve.name == "AA"
        }
        self.edges = {}
        self.find_edges()

    def parse(self):
        """
        Initialize the dictionary of valve_objects from the input data
        """
        in_file = open(self.data, "r", encoding="utf-8")
        with open(self.data, encoding="utf-8") as in_file:
            input_data = in_file.read()
        split_lines = [
            findall(r"[A-Z\d]+", line)[1:] for line in split(r"\n", input_data)
        ]
        self.valves = {
            name: Valve(name, int(flow_rate), neighbors)
            for name, flow_rate, *neighbors in split_lines
        }

    def reset_visited(self):
        """
        Reset the visited attribute to false for all valves in the cave
        """
        for valve in self.valves.values():
            valve.visited = False

    def find_edges(self):
        """
        Conduct a breadth first search to find the all distances
        between valves with non zero flow rates/start valve AA
        """
        for name, valve in self.valves_not_zero.items():
            valve_queue = deque([(0, valve)])
            valve.visited = True
            # reset for next valve
            while valve_queue:
                length, start_valve = valve_queue.popleft()
                for neighbor in start_valve.neighbors:
                    if self.valves[neighbor].visited:
                        continue
                    self.valves[neighbor].visited = True
                    if self.valves[neighbor].flow_rate:
                        self.edges[frozenset([name, neighbor])] = length + 1
                    valve_queue.append((length + 1, self.valves[neighbor]))
            self.reset_visited()

cavegraph_1 = CaveGraph("2022/day_16/input_test.txt")
print(cavegraph_1.edges)
