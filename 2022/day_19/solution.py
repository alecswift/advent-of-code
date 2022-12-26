# possible options at each minute, doesn't begin until you can construct a robot (clay or ore depending on blueprint)
# construct clay robot or ore robot
# options once you have sufficient clay:
# construct clay robot, ore robot, or obsidien robot
# options once you have sufficient obsidian
# construct clay robot, ore robot, obsidien robot, or geode robot
# depth first search, states as the nodes which go in cache: robots, ore, time remaining previous options depending on state which diverge the path
# find the amount geodes for each path
# find the max amount 
# states = amount of ore, amount of robots, time remaining
# (time remaining, (ore robots, clay robots, obsidian robots, geode robots), (ore, clay, obsidian, geodes))

def search(rem_time, robots, ores):
    