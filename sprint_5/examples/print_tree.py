def print_forward(root) -> None:
    print(root.value)
    for child in root.children:
        print_forward(child)


def print_backward(root) -> None:
    for child in root.children:
        print_backward(child)
    print(root.value)


def print_LMR(root) -> None:
    if root.left is not None:
        print_LMR(root.left)
    print(root.value)
    if root.right is not None:
        print_LMR(root.right)
