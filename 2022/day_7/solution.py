"""
Find the total size of all directories that have a size 
of less than 100,000 from file system browsing data
"""

from typing import TextIO, Type


class Node:
    """
    Class that represents a node (directory) in a file tree
    the node has the attributes parent (outer directory), name,
    inner directories, files, and indirect file size
    """

    def __init__(self, name: str) -> None:
        self.parent: Type[Node] | None = None
        self.name: str = name
        self.inner_dirs: list[str] = []
        self.files: list[tuple[str, str]] = []
        self.indirect_size: int = 0

    def direct_file_size(self) -> int:
        """Return the direct file size of the node object"""
        return sum([int(size) for size, _ in self.files])


def parse(input_file: str) -> list[str]:
    """Return a list of lines from file system browsing data"""
    in_file: TextIO = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    return input_data.split("\n")
