# doubly linked list or collections deque
# pop item rotate (or traverse linked list) to wanted position insert item
from collections import deque
from itertools import cycle



def parse(input_file):
    in_file = open(input_file, 'r', encoding = 'utf-8')
    with open(input_file, encoding = 'utf-8') as in_file:
        input_data = in_file.read()
    split_lines = input_data.split('\n')
    coords = [(int(line), index) for index, line in enumerate(split_lines)]
    multiplied_coords = [(value * 811589153, index) for value, index in coords]
    return coords, multiplied_coords


def decrypt(coords):
    queue_coords = deque(coords)
    for coord in coords:
        current_index = queue_coords.index(coord)
        queue_coords.remove(coord)
        queue_coords.rotate(-coord[0])
        queue_coords.insert(current_index, coord[0])
    return list(queue_coords)

def cycles(sorted_coords):
    count = None
    numbers = []
    for coord in cycle(sorted_coords):
        if len(numbers) == 3:
            break
        if count is not None:
            count += 1
            if (count != 0) and (count % 1000 == 0):
                numbers.append(coord)
        elif coord == 0:
            count = 0
    return sum(numbers)



coords_1, multiplied_coords_1 = parse('2022/day_20/input.txt')
sorted_coords_1 = decrypt(coords_1)
#print(sorted_coords_1)
print(cycles(sorted_coords_1))
