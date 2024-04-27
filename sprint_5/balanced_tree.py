# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def get_height(root) -> int:
    if root.left is None and root.right is None:
        return 1

    return 1 + max(get_height(root.left) if root.left else 0, get_height(root.right) if root.right else 0)


def solution(root) -> bool:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    left_len = 0
    if root.left is not None:
        left_len = get_height(root.left)

    right_len = 0
    if root.right is not None:
        right_len = get_height(root.right)

    diff = left_len - right_len

    if abs(diff) <= 1 and solution(root.right) is True and solution(root.left) is True:
        return True
    return False


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5) == True


if __name__ == "__main__":
    test()
