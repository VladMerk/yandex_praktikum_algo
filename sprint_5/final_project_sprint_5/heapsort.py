"""

"""
from dataclasses import dataclass, field


@dataclass
class User:
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
        return self.name


@dataclass
class Heap:
    heap: list[User] = field(default_factory=list)

    def parent(self, index: int) -> int:
        return index // 2

    def left_child(self, index: int) -> int:
        return 2 * index

    def right_child(self, index: int) -> int:
        return 2 * index + 1

    def sift_up(self, index: int) -> None:
        if index == 0:
            return

        parent_index = self.parent(index)
        if self.heap[parent_index] < self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self.sift_up(parent_index)

    def sift_down(self, index: int) -> None:
        largest: int = index
        left: int = self.left_child(index)
        right: int = self.right_child(index)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.sift_down(largest)

    def insert(self, value: User) -> None:
        self.heap.append(value)
        index: int = len(self.heap) - 1
        self.sift_up(index)

    def pop(self) -> User:
        result = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.sift_down(0)
        return result


if __name__ == "__main__":
    n = int(input())

    heap = Heap()

    for _ in range(n):
        login, tasks, penalty = input().strip().split()
        heap.insert(User(login, int(tasks), int(penalty)))

    for _ in range(n):
        print(heap.pop())
