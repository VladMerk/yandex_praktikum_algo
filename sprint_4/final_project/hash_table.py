from typing import Optional


class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value: int = value
        self._next: Optional["Node"] = None


class HashArr:
    def __init__(self, value: int | None = None) -> None:
        self._head: Node | None = None

    def add(self, key: int, value: int) -> None:
        if self._head is None:
            self._head = Node(key, value)
            return

        if self._head.key == key:
            self._head.value = value
            return

        node: Node | None = self._head
        while node._next:
            if node.key == key:
                node.value = value
                return
            node = node._next
        node._next = Node(key, value)

    def get(self, key: int) -> int | None:
        node: Node | None = self._head
        while node:
            if node.key == key:
                return node.value
            node = node._next
        return None

    def delete(self, key: int) -> int | None:
        if self._head is None:
            return None

        if self._head.key == key:
            value = self._head.value
            self._head = self._head._next
            return value

        prev_node: Node = self._head
        current_node: Node | None = prev_node._next
        while current_node:
            if current_node.key == key:
                value: int = current_node.value
                prev_node._next = current_node._next
                return value
            prev_node = current_node
            current_node = current_node._next
        return None


class HashTable:
    def __init__(self, size: int = 10 ** 5 - 1):
        self.max_size: int = size
        self.items: list[HashArr] = [HashArr() for _ in range(self.max_size)]

    def _get_bucket(self, value) -> int:
        return value % self.max_size

    def get(self, key: int) -> int | None:
        item: HashArr | None = self.items[self._get_bucket(key)]
        return item.get(key)

    def put(self, key: int, value: int) -> None:
        bucket: int = self._get_bucket(key)
        self.items[bucket].add(key, value)

    def delete(self, key: int) -> int | None:
        bucket: int = self._get_bucket(key)
        return self.items[bucket].delete(key)


def main():
    n = int(input())
    table = HashTable()

    while n > 0:
        commands: list = input().split()
        match commands[0]:
            case "put":
                table.put(key=int(commands[1]), value=int(commands[2]))
            case "get":
                print(table.get(key=int(commands[1])))
            case "delete":
                print(table.delete(key=int(commands[1])))
        n -= 1


if __name__ == "__main__":
    main()
