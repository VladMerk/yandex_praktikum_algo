class Node:
    def __init__(self, value, left=None, right=None):
        self.value: int = value
        self.right: Node | None = right
        self.left: Node | None = left


def solution(root: Node) -> int:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    if root.left is None and root.right is None:
        return root.value

    if root.left is not None:
        left_value = solution(root.left)
    else:
        left_value = 0

    if root.right is not None:
        right_value: int = solution(root.right)
    else:
        right_value = 0

    return max(root.value, left_value, right_value)


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == "__main__":
    test()
