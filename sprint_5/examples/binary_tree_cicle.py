class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # высота узла, начальное значение - 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if not root:
            return TreeNode(value)

        # Используем стек для обхода дерева и вставки значения
        stack = []
        current = root
        while True:
            stack.append(current)
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(value)
                    break
                else:
                    current = current.right

        # Обновляем высоты узлов вдоль пути вверх
        while stack:
            node = stack.pop()
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
            # Перебалансируем, если необходимо
            self.balance(node)

        return root

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        # Поворот
        y.right = z
        z.left = T3

        # Обновление высот
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Поворот
        y.left = z
        z.right = T2

        # Обновление высот
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def balance(self, node):
        balance = self.get_balance(node)

        if balance > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def search(self, root, value):
        if not root:
            return None

        # Используем цикл для поиска значения
        current = root
        while current:
            if current.value == value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return None


# Пример использования:
avl_tree = AVLTree()
root = None
values = [9, 5, 10, 0, 6, 11, -1, 1, 2]
for value in values:
    avl_tree.insert(root, value)

# Поиск значения
target = 10
result = avl_tree.search(root, target)
if result:
    print("Значение {} найдено в дереве.".format(target))
else:
    print("Значение {} не найдено в дереве.".format(target))
