"""
Find the total size of all directories that have a size
of less than 100,000 from file system browsing data
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

    def direct_file_size(self) -> int:
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
        node: Node = Node(name, parent)
        node.parent = parent
        self.nodes.append(node)
        return node

    def direct_sizes(self) -> list[tuple[Type[Node], int]]:
        """
        Return a list of nodes with direct sizes that
        are under 100,000 from the list of nodes
        """
        dir_sizes: list[tuple[Type[Node], int]] = []
        for node in self.nodes:
            if 0 < node.direct_file_size() <= 100000:
                dir_sizes.append((node, node.direct_file_size()))
        return dir_sizes

    def indirect_sizes(self) -> None:
        """Initialize the indirect size attribute of all nodes"""
        for node in self.nodes:
            parent: Type[Node] = node.parent
            while parent:
                size: int = node.direct_file_size()
                parent.indirect_size += size
                parent = parent.parent


def parse(input_file: str) -> list[str]:
    """Return a list of lines from file system browsing data"""
    in_file: TextIO = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    return input_data.split("\n")
