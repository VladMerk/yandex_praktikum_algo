"""
-- ПРИНЦИП РАБОТЫ --
Алгоритм удаления узла из бинарного дерева работает путем замены удаляемого узла на подходящий узел из дерева,
чтобы сохранить структуру и порядок значений. Если удаляемый узел имеет обоих потомков,
мы заменяем его на наименьший узел в его правом поддереве. В случае отсутствия правого поддерева,
узел заменяется на его левого потомка.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Поиск удаляемого узла в бинарном дереве занимает время O(H), где H - высота дерева.
Затем процесс замены узла также требует времени O(H), так как находится наименьший узел в поддереве.
Таким образом, временная сложность удаления узла из бинарного дерева составляет O(H), где H - высота дерева.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Для хранения ссылок на узлы и их значений требуется память O(1).
Однако при рекурсивном проходе по дереву используется дополнительная память в стеке вызовов функций,
что занимает O(H) памяти, где H - высота дерева.

Посылка: https://contest.yandex.ru/contest/24810/run-report/113556584/

"""
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: "Node"
    right: "Node"


def min_value_node(node: Node) -> Node:
    current: Node = node

    while current.left is not None:
        current = current.left

    return current


def remove(root, key: int) -> Node | None:
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

        node: Node = min_value_node(root.right)

        root.value = node.value
        root.right = remove(root.right, node.value)

    return root
