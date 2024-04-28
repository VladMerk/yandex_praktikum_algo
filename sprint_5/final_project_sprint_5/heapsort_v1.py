from dataclasses import dataclass, field


@dataclass
class User:
    """Класс описания стажера."""

    name: str
    tasks: int
    penalty: int

    def __gt__(self, other: "User") -> bool:
        if self.tasks != other.tasks:
            return self.tasks > other.tasks
        elif self.penalty != other.penalty:
            return self.penalty < other.penalty
        else:
            return self.name < other.name

    def __repr__(self) -> str:
        """Метод для вывода объекта при печати в терминале."""
        return self.name


@dataclass
class Heap:
    heap: list[User] = field(default_factory=list)

    def parent(self, index: int) -> int:
        return (index - 1) // 2

    def left_child(self, index: int) -> int:
        return 2 * index + 1

    def right_child(self, index: int) -> int:
        return 2 * index + 2

    def insert(self, value: User) -> None:
        self.heap.append(value)
        index: int = len(self.heap) - 1
        parent_index: int = self.parent(index)
        while index > 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = self.parent(index)

    def sift_up(self, index: int) -> None:
        if index == 0:
            return

        parent_index: int = self.parent(index)

        if self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.sift_up(self.parent(index))

    def sift_down(self, index: int) -> None:
        left_index: int = self.left_child(index)
        right_index: int = self.right_child(index)

        heap_size: int = len(self.heap) - 1

        if heap_size < left_index:
            return

        if right_index <= heap_size and self.heap[left_index] < self.heap[right_index]:
            largest: int = right_index
        else:
            largest: int = left_index

        if self.heap[index] > self.heap[largest]:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]

            self.sift_down(largest)

    def pop(self) -> User | None:
        if len(self.heap) == 0:
            return None

        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.sift_down(0)
        return root


# if __name__ == "__main__":
#     n = int(input())

#     heap = Heap()

#     for i in range(n):
#         login, tasks, penalty = input().strip().split()

#         heap.insert(User(name=login, tasks=int(tasks), penalty=int(penalty)))

#         heap.sift_up(i)

#     for _ in range(n):
#         print(heap.pop())

if __name__ == "__main__":
    heap = Heap()
    heap.insert(User("alla", 4, 100))
    heap.insert(User("gena", 6, 1000))
    heap.insert(User("gosha", 2, 90))
    heap.insert(User("rita", 2, 90))
    heap.insert(User("timofey", 4, 80))

    sorted_users = []

    while heap.heap:
        sorted_users.append(heap.pop())

    for user in sorted_users:
        print(user.name)

