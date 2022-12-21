"""
Find the optimal path through a cave with valves
such that valves are opened in the order that
releases the most pressure in 30 minutes
"""

from collections import deque
from copy import deepcopy
from re import split, findall

cache = {}

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
            name: valve for name, valve in self.valves.items() if valve.flow_rate
        }
        self.lengths = {}
        self.find_lengths()
        self.indices = {name: index for index, name in enumerate(self.valves_not_zero)}

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

    def find_lengths(self):
        """
        Conduct a breadth first search to find the all distances
        between valves with non zero flow rates/start valve AA
        """
        valves_to_check = deepcopy(self.valves_not_zero)
        valves_to_check["AA"] = self.valves["AA"]
        for name, valve in valves_to_check.items():
            valve_queue = deque([(0, valve)])
            valve.visited = True
            self.lengths[name] = {name: 0, "AA": 0}
            # reset for next valve
            while valve_queue:
                length, start_valve = valve_queue.popleft()
                for neighbor in start_valve.neighbors:
                    if self.valves[neighbor].visited:
                        continue
                    self.valves[neighbor].visited = True
                    if self.valves[neighbor].flow_rate:
                        # maybe an issue with multiple paths but i don't think so
                        self.lengths[name][neighbor] = length + 1
                    valve_queue.append((length + 1, self.valves[neighbor]))
            self.reset_visited()
            del self.lengths[name][name]
            if name != "AA":
                del self.lengths[name]["AA"]

    def depth_first_search(self, time, current_valve, valves_open):
        """
        Perform a depth first search on the relevant nodes to find
        the max pressure released given a start time, start valve,
        and valves that are open
        """
        if (time, current_valve, valves_open) in cache:
            return cache[(time, current_valve, valves_open)]
        max_pressure = 0
        for neighbor in self.lengths[current_valve]:
            bit = 1 << self.indices[neighbor]
            if valves_open & bit:
                continue
            time_rem = time - self.lengths[current_valve][neighbor] - 1
            if time_rem <= 0:
                continue
            max_pressure = max(
                max_pressure,
                self.depth_first_search(time_rem, neighbor, valves_open | bit)
                + (self.valves_not_zero[neighbor].flow_rate * time_rem),
            )
        cache[(time, current_valve, valves_open)] = max_pressure
        return max_pressure


cavegraph_1 = CaveGraph("2022/day_16/input.txt")
print(cavegraph_1.depth_first_search(30, 'AA', 0))
