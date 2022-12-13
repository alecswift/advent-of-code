from typing import TextIO

class TreeMatrix:

    def __init__(self, rows):
        self.rows = rows
        self.columns = [[]]
        self.trees = {}
        self.num_rows = len(rows)
        self.num_cols = len(rows[0])

    def set_columns(self, count = 0):
        for row in self.rows:
            self.columns[count].append(row[count])
        if count < len(self.rows) - 1:
            self.columns.append([])
            count += 1
            return self.set_columns(count)
        return self.columns

    def remove_edges(self):
        return {
            tree_position: value for tree_position, value in self.trees.items()
            if (tree_position[1] not in (1, self.num_cols))
            and (tree_position[0] not in (1, self.num_rows))
        }
    
    def left_right(self, tree_position):
        row_num, column_num = tree_position
        row = self.rows[row_num - 1]
        left = row[:column_num - 1]
        right = row[column_num:]
        return left[::-1], right

    def up_down(self, tree_position):
        row_num, column_num = tree_position
        column = self.columns[column_num - 1]
        up = column[:row_num - 1]
        down = column[row_num:]
        return up[::-1], down


    def is_visible(self, tree_position):
        up, down = self.up_down(tree_position)
        left, right = self.left_right(tree_position)
        cross_section = sorted(up), sorted(down), sorted(left), sorted(right)
        for direction in cross_section:
            if direction:
                if self.trees[tree_position] <= direction[-1]:
                    continue
            return True
        return False


def parse(input_file: str):
    in_file: TextIO = open(input_file, 'r', encoding = 'utf-8')
    with open(input_file, encoding = 'utf-8') as in_file:
        input_data: str = in_file.read()
    split_lines = input_data.split('\n')
    parsed_data = [list(map(int, list(line))) for line in split_lines]
    return parsed_data

def build_matrix(input_file):
    data = parse(input_file)
    tree_matrix = TreeMatrix(data)
    for row_num, row in enumerate(data):
        for column_num, value in enumerate(row):
            tree_matrix.trees[(row_num + 1, column_num + 1)] = value
    tree_matrix.set_columns()
    return tree_matrix

def num_of_visible_trees(tree_matrix):
    visible_trees = 0
    inner_trees = tree_matrix.remove_edges()
    for position in inner_trees:
        if tree_matrix.is_visible(position):
            visible_trees += 1
    visible_trees += (tree_matrix.num_rows * 2) + (tree_matrix.num_cols * 2) - 4
    return visible_trees

def max_scenic_score(tree_matrix):
    scores = []
    trees = tree_matrix.remove_edges()
    for tree_position, value in trees.items():
        up, down = tree_matrix.up_down(tree_position)
        left, right = tree_matrix.left_right(tree_position)
        cross_section = up, down, left, right
        product = 1
        for direction in cross_section:
            count = 0
            for value_1 in direction:
                count += 1
                if value_1 >= value:
                    product *= count
                    break
            else:
                product *= count
        scores.append(product)
    return sorted(scores)[-1]

tree_matrix_1 = build_matrix('2022/day_8/input.txt')
print(num_of_visible_trees(tree_matrix_1))
print(max_scenic_score(tree_matrix_1))
