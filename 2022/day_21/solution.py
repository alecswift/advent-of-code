"""
Find the value of mathematical expressions that are
represented as trees from the given input data
"""
from collections import deque
from re import findall


class Node:
    """
    Represents an node of the tree. Internal nodes
    have children and an operator value. Leaves have
    no children and a variable or numeric value
    """

    def __init__(self, value, children):
        self.value = value
        self.children = children


class Tree:
    """
    Represents a tree with nodes as the vertices.
    Builds the post fix expression for the tree
    """

    def __init__(self, input_file):
        self.input_file = input_file
        self.data = None
        self.parse()
        self.nodes = {}
        self.insert_nodes()
        self.post_fix = []

    def parse(self):
        """Initializes the data attribute by parsing the input_file"""
        with open(self.input_file, encoding="utf-8") as in_file:
            input_data = in_file.read()
        self.data = findall(r"(\w+): (.+)", input_data)

    def insert_nodes(self):
        """Inserts nodes from the parsed data"""
        for name, job in self.data:
            if job.isdigit():
                self.nodes[name] = Node(int(job), [])
            else:
                left, operator, right = findall(r"([a-z]+) (.) ([a-z]+)", job)[0]
                self.nodes[name] = Node(operator, [left, right])

    def post_fix_expr(self, current_root):
        """Post order tree traversal to initialize the post fix expression"""
        for child in current_root.children:
            node = self.nodes[child]
            self.post_fix_expr(node)
        self.post_fix.append(current_root.value)


def operation(operator, num_1, num_2):
    """
    Returns the result of a mathematical operation
    from the given operator and numbers
    """
    match operator:
        case "-":
            return num_1 - num_2
        case "+":
            return num_1 + num_2
        case "/":
            return num_1 / num_2
        case "*":
            return num_1 * num_2


def evaluate(post_fix_expr):
    """
    Returns the numeric result of solving a post fix expression
    """
    queue = deque()
    for element in post_fix_expr:
        if isinstance(element, int):
            queue.append(element)
        else:
            num_2 = queue.pop()
            num_1 = queue.pop()
            queue.append(operation(element, num_1, num_2))
    return int(queue[0])


tree_1 = Tree("2022/day_21/input.txt")
root = tree_1.nodes["root"]
tree_1.post_fix_expr(root)
print(evaluate(tree_1.post_fix))


def split(tree):
    """
    Returns a numeric value of one side of a tree
    and the root of the other side depending on which
    side the variable 'y' is located
    """
    root.value = "="
    tree.nodes["humn"].value = "y"
    right_tree_root = tree.nodes[root.children[1]]
    left_tree_root = tree.nodes[root.children[0]]

    tree_1.post_fix = []
    tree.post_fix_expr(right_tree_root)
    if "y" not in tree.post_fix:
        right_value = evaluate(tree.post_fix)
        return right_value, left_tree_root

    tree.post_fix = []
    tree.post_fix_expr(left_tree_root)
    if "y" not in tree.post_fix:
        left_value = evaluate(tree.post_fix)
        return left_value, right_tree_root


def part_2(tree):
    """
    Returns the value of the variable y. Y is the number that
    makes both sub trees evaluate to the the same number
    """
    sub_tree_value, sub_tree_root = split(tree)
    queue_1 = deque([sub_tree_root])
    while queue_1[0].value != "y":
        left_or_right = None
        left, right = queue_1[0].children

        tree.post_fix = []
        tree.post_fix_expr(tree.nodes[left])
        if "y" not in tree.post_fix:
            tree.nodes[left].value = evaluate(tree.post_fix)
            tree.nodes[left].children = []
            left_or_right = "right"

        tree.post_fix = []
        tree.post_fix_expr(tree.nodes[right])
        if "y" not in tree.post_fix:
            tree.nodes[right].value = evaluate(tree.post_fix)
            tree.nodes[right].children = []
            left_or_right = "left"

        operator = None
        match queue_1[0].value:
            case "+":
                operator = "-"
            case "-":
                operator = "+"
            case "*":
                operator = "/"
            case "/":
                operator = "*"

        if left_or_right == "left":
            queue_1.append(tree.nodes[left])
            sub_tree_value = operation(
                operator, sub_tree_value, tree.nodes[right].value
            )
        if left_or_right == "right":
            if operator == "+":
                queue_1.append(tree.nodes[right])
                sub_tree_value = operation("-", tree.nodes[left].value, sub_tree_value)
            elif operator == "*":
                queue_1.append(tree.nodes[right])
                sub_tree_value = operation("/", tree.nodes[left].value, sub_tree_value)
            else:
                queue_1.append(tree.nodes[right])
                sub_tree_value = operation(
                    operator, sub_tree_value, tree.nodes[left].value
                )
        queue_1.popleft()
    return int(sub_tree_value)


print(part_2(tree_1))
