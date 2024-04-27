from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    height: int = 1


class AVLTree:
    def __init__(self) -> None:
        self.root: Node | None = None

    def get_height(self, node: Node | None) -> int:
        if not node:
            return 0
        return node.height

    def get_balance(self, node: Node) -> int:
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def _rotate_right(self, z: Node) -> Node:
        y: Node = z.left
        T3: Node = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def _rotate_left(self, z: Node) -> Node:
        y: Node = z.right
        T2: Node = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def _insert(self, root: Node | None, value: int) -> Node:
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance: int = self.get_balance(root)

        # Left Left Case
        if balance > 1 and value > root.left.value:
            return self._rotate_right(root)

        # Right Right Case
        if balance < -1 and value > root.right.value:
            return self._rotate_left(root)

        # Left Right Case
        if balance > 1 and value > root.left.value:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        # Right Left Case
        if balance < -1 and value < root.right.value:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root
