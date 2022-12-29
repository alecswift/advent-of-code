# All i need to do is replace sibling of x with evaled number
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
root = tree.nodes['root']
tree.post_fix_expr(root)
print(eval(tree.post_fix))
tree.post_fix = []

root.value = '='
tree.nodes['humn'].value = 'y'
right_tree_root = tree.nodes[root.children[1]]
left_tree_root = tree.nodes[root.children[0]]
tree.post_fix_expr(right_tree_root)

right_value = eval(tree.post_fix)
queue_1 = deque([left_tree_root])
while queue_1[0].value != 'y':
    left_or_right = None
    left, right = queue_1[0].children
    tree.post_fix = []
    tree.post_fix_expr(tree.nodes[left])
    if 'y' not in  tree.post_fix:
        tree.nodes[left].value = eval(tree.post_fix)
        tree.nodes[left].children = []
        left_or_right = 'right'
    tree.post_fix = []
    tree.post_fix_expr(tree.nodes[right])
    if 'y' not in  tree.post_fix:
        tree.nodes[right].value = eval(tree.post_fix)
        tree.nodes[right].children = []
        left_or_right = 'left'
    operator = None
    match queue_1[0].value:
        case '+':
            operator = '-'
        case '-':
            operator = '+'
        case '*':
            operator = '/'
        case '/':
            operator = '*'
    if left_or_right == 'left':
        queue_1.append(tree.nodes[left])
        right_value = operation(operator, right_value, tree.nodes[right].value)
    if left_or_right == 'right':
        if operator == '+':
            queue_1.append(tree.nodes[right])
            right_value = operation('-', tree.nodes[left].value, right_value)
        elif operator == '*':
            queue_1.append(tree.nodes[right])
            right_value = operation('/', tree.nodes[left].value, right_value)
        else:
            queue_1.append(tree.nodes[right])
            right_value = operation(operator, right_value, tree.nodes[left].value)
    queue_1.popleft()
print(right_value)



