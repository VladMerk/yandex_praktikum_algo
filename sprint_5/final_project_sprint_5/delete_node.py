def min_value_node(node):
    current = node

    while current.left is not None:
        current = current.left

    return current


def remove(root, key):
    if root is None:
        return root

    if key < root.value:
        root.left = remove(root.left, key)
    elif key > root.value:
        root.right = remove(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        node = min_value_node(root.right)

        root.value = node.value
        root.right = remove(root.right, node.value)

    return root
