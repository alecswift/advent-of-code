# be thoughtful of coordinates y = row number in array, x = column number

class HorLineRock:
    
    def __init__(self, row):
        # row is the highest rock, points initialized three rows above
        self.position = [[2, row + 4], [3, row + 4], [4, row + 4], [5, row + 4]]

class PlusRock:
    
    def __init__(self, row):
        self.position = [[2, row + 5], [3, row + 5], [3, row + 4], [3, row + 6], [4, row + 5]]

class LRock:
    def __init__(self, row):
        self.position = [[2, row + 4], [3, row + 4], [4, row + 4], [4, row + 5], [4, row + 6]]

class VertLineRock:
    def __init__(self, row):
        self.position = [[2, row + 4], [2, row + 5], [2, row + 6], [2, row + 7]]

class SquareRock:
    def __init__(self, row):
        self.position = [[2, row + 4], [3, row + 4], [2, row + 5], [3, row + 5]]


# display test
array = [['.'] * 7 for _ in range(8)]
for num in range(7):
    array[0][num] = '#'
rocks = [HorLineRock(0), SquareRock(0), PlusRock(0), LRock(0), VertLineRock(0)]
for rock in rocks:
    for x, y in rock.position:
        array[y][x] = '#'
    # print('\n'.join([''.join(line) for line in array[::-1]]))
    array = [['.'] * 7 for _ in range(8)]
    for num in range(7):
        array[0][num] = '#'