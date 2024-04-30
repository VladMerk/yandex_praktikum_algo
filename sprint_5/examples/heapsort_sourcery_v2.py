from dataclasses import dataclass


@dataclass
class User:
    name: str
    tasks: int
    penalty: int

    def __lt__(self, other: "User") -> bool:
        if self.tasks != other.tasks:
            return self.tasks < other.tasks
        elif self.penalty != other.penalty:
            return self.penalty < other.penalty
        else:
            return self.name < other.name

    def __repr__(self) -> str:
        return self.name


class HeapSort:
    def __init__(self):
        self.heap = []

    def insert(self, user: User):
        self.heap.append(user)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, index):
        if index == 0:
            return

        parent_index = (index - 1) // 2
        if self.heap[parent_index] < self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._sift_up(parent_index)

    def _sift_down(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.heap[l] > self.heap[largest]:
            largest = l

        if r < n and self.heap[r] > self.heap[largest]:
            largest = r

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._sift_down(n, largest)

    def heapify(self):
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(n, i)

    def sort(self):
        self.heapify()
        n = len(self.heap)
        for i in range(n - 1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            self._sift_down(i, 0)


# Example usage
heap_sorter = HeapSort()
heap_sorter.insert(User("alla", 4, 100))
print("Sorted users after inserting Alice:")
for user in heap_sorter.heap:
    print(user)

heap_sorter.insert(User("timofey", 4, 80))
print("\nSorted users after inserting Bob:")
for user in heap_sorter.heap:
    print(user)

heap_sorter.insert(User("gena", 6, 1000))
print("\nSorted users after inserting Charlie:")
for user in heap_sorter.heap:
    print(user)

heap_sorter.insert(User("rita", 2, 10))
print("\nSorted users after inserting Charlie:")
for user in heap_sorter.heap:
    print(user)
