from itertools import combinations

with open("2015/day_17/input.txt", encoding = "utf-8") as in_file:
    input_data = in_file.read()

data = [int(num) for num in input_data.split("\n")]

combos = 0
combos_min_containers = 0
first_hit = False
min_containers = -1
for num in range(len(data)):
    for combo in combinations(data, num):
        if sum(combo) == 150:
            combos += 1
            if not first_hit:
                min_containers = num
                first_hit = True
    if num == min_containers:
        combos_min_containers = combos
            

print(combos)
print(combos_min_containers)
