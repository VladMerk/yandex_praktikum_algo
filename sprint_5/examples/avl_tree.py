from typing import Optional


class Node:
    def __init__(self, key, height=1, left: Optional["Node"] = None, right: Optional["Node"] = None) -> None:
        self.key = key
        self.left: Optional["Node"] = left
        self.right = right
        self.height = height


def small_left_rotation(a: Node):
    # Задаём обозначения.
    b = a.right
    C = b.left

    # Переусыновляем вершины.
    a.right = C
    b.left = a

    # Корректируем высоты в зависимости от того, равны ли высоты C и R.
    if C.height == R.height:
        a.height -= 1
        b.height += 1
    else:
        a.height -= 2

    # Возвращаем новый корень.
    return b


def big_left_rotation(a: Node):
    # Задаём обозначения.
    b = a.right
    c = b.left
    M = c.left
    N = c.right

    # Переусыновляем вершины.
    a.right = M
    b.left = N
    c.left = a
    c.right = b

    # Корректируем высоты.
    a.height -= 2
    b.height -= 1
    c.height += 1

    # Возвращаем новый корень.
    return c


# Функция возвращает новый корень поддерева.
def rotate(vertex):
    if abs(vertex.left.height - vertex.right.height) < 2:
        # Вращать не надо, поддерево с вершиной vertex и так сбалансировано.
        return vertex
    if vertex.left.height - vertex.right.height == -2:
        # Нам нужны левые вращения.
        b = vertex.right
        R = b.right
        C = b.left

        if C.height <= R.height:
            # Нужно малое левое вращение.
            return small_left_rotation(vertex)
        else:
            # Нужно большое левое вращение.
            return big_left_rotation(vertex)

    if vertex.left.height - vertex.right.height == 2:
        # Нам нужны правые вращения.
        b = vertex.left
        C = b.right
        L = b.left

        if C.height <= L.height:
            # Нужно малое правое вращение.
            return small_right_rotation(vertex)
        else:
            # Нужно большое правое вращение.
            return big_right_rotation(vertex)
