"""
Find the total size of all directories that have a size of
less than 100,000 from file system browsing data. Find the
size of the smallest directory in the file system that can
be deleted to free up enough space for the update
"""

from typing import TextIO, Type
from re import findall


class Node:
    """
    Class that represents a node (directory) in a file tree
    the node has the attributes parent (outer directory), name,
    inner directories, files, and indirect file size
    """

    def __init__(self, name, parent) -> None:
        self.parent: Type[Node] = parent
        self.name: str = name
        self.inner_dirs: list[str] = []
        self.files: list[tuple[str, str]] = []
        self.indirect_size: int = 0

    def direct_size(self) -> int:
        """Return the direct file size of the node object"""
        return sum([int(size) for size, _ in self.files])


class FileTree:
    """Represents a file tree with the attribute nodes"""

    def __init__(self) -> None:
        self.nodes: list[Type[Node]] = []

    def add_node(self, data: tuple[str, Type[Node]]) -> Node:
        """Create a node with name and parent initialized"""
        name: str
        parent: Type[Node]
        name, parent = data
        node: Type[Node] = Node(name, parent)
        node.parent = parent
        self.nodes.append(node)
        return node

    def direct_sizes(self) -> list[int]:
        """
        Return a list of direct sizes of nodes
        """
        return [node.direct_size() for node in self.nodes]

    def indirect_sizes(self) -> list[int]:
        """Initialize the indirect size attribute of all nodes"""
        for node in self.nodes:
            parent: Type[Node] = node.parent
            while parent:
                size: int = node.direct_size()
                parent.indirect_size += size
                parent = parent.parent
        return [node.indirect_size for node in self.nodes]

    def sizes(self):
        """
        Return the total file size of the entire system
        of directories with file sizes less than 100,000
        """
        sizes = zip(self.direct_sizes(), self.indirect_sizes())
        return [sum(size) for size in sizes]

    def used_space(self):
        """
        Return the total amount of used space in the file system
        """
        return sum(node.direct_size() for node in self.nodes)

    def size_dir_to_del(self):
        """
        Return the size of the smallest directory in the file system
        that can be deleted to free up enough space for the update
        """
        space_for_update = 30000000 - (70000000 - self.used_space())
        smallest = self.sizes()[0]
        for size in self.sizes():
            if size < space_for_update:
                continue
            if size < smallest:
                smallest = size
        return smallest

def parse(input_file: str) -> list[str]:
    """Return a list of lines from file system browsing data"""
    in_file: TextIO = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    return input_data.split("\n")


def build_tree(input_file: str) -> Type[FileTree]:
    """
    Create a FileTree object with the given terminal browsing data
    """
    data: list[str] = parse(input_file)
    file_tree_1 = FileTree()
    current_node = None
    parent_node = None
    for line in data:
        if "$ cd .." in line:
            current_node = current_node.parent
        elif "$ cd" in line:
            current_dir: str = line[5:]
            parent_node = current_node
            node_data: tuple[str, type[Node] | None] = current_dir, parent_node
            current_node = file_tree_1.add_node(node_data)
        elif "$ ls" in line:
            continue
        elif line.startswith("dir "):
            (current_node.inner_dirs).append(line[4:])
        else:
            (current_node.files).append(findall(r"(\d+) (\D+)", line)[0])
    return file_tree_1


file_tree_data = build_tree("2022/day_7/input.txt")
print(sum(size for size in file_tree_data.sizes() if size <= 100000))
print(file_tree_data.size_dir_to_del())
