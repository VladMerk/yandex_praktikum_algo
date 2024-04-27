from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional["Node"] = None, right: Optional["Node"] = None) -> None:
        self.value: int = value
        self.left = left
        self.right = right


def insert_node(root: Node, key: int):
    if root is None:
        return Node(key)

    if key < root.value:
        root.left = insert_node(root.left, key)
    elif key >= root.value:
        root.right = insert_node(root.right, key)

    return root
