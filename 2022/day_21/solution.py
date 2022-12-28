# start at root
# go all the way left
# save leaf to queue
# go to parent of leaf and save operator to queue
# go full left down parent
# start from root and recursively perform operator function on children
# depth first traversal to get postfix expression
from collections import deque
from re import findall


class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children


class Tree:
    def __init__(self, input_file):
        self.input_file = input_file
        self.data = None
        self.parse()
        self.nodes = {}
        self.insert_nodes()
        self.post_fix = []
        self.post_fix_expr(self.nodes['root'])

    def parse(self):
        in_file = open(self.input_file, "r", encoding="utf-8")
        with open(self.input_file, encoding="utf-8") as in_file:
            input_data = in_file.read()
        self.data = findall(r"(\w+): (.+)", input_data)

    def insert_nodes(self):
        for name, job in self.data:
            if job.isdigit():
                self.nodes[name] = Node(int(job), [])
            else:
                left, operator, right = findall(r"([a-z]+) (.) ([a-z]+)", job)[0]
                self.nodes[name] = Node(operator, [left, right])

    def post_fix_expr(self, root):
        for child in root.children:
            node = self.nodes[child]
            self.post_fix_expr(node)
        self.post_fix.append(root.value)

def operation(operator, num_1, num_2):
    match operator:
        case '-':
            return num_1 - num_2
        case '+':
            return num_1 + num_2
        case '/':
            return num_1 / num_2
        case '*':
            return num_1 * num_2

def eval(post_fix_expr):
    queue = deque()
    for element in post_fix_expr:
        if isinstance(element, int):
            queue.append(element)
        else:
            num_2 = queue.pop()
            num_1 = queue.pop()
            queue.append(operation(element, num_1, num_2))
    return int(queue[0])



tree = Tree('2022/day_21/input.txt')
print(eval(tree.post_fix))
