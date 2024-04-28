class MinHeap:
    def __init__(self) -> None:
        self.heap: list[int] = []

    def __len__(self):
        return len(self.heap)

    def parent(self, index) -> int:
        return (index - 1) // 2

    def left_child(self, index) -> int:
        return 2 * index + 1

    def right_child(self, index) -> int:
        return 2 * index + 2

    def insert(self, value):
        self.heap.append(value)
        i: int = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def heapify(self, index):
        smallest = index
        left: int = self.left_child(index)
        right: int = self.right_child(index)
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify(smallest)

    def extract_min(self):
        if len(self.heap) == 0:
            return None

        root: int = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapify(0)
        return root

    def get_min(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]


if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(3)
    heap.insert(6)
    heap.insert(2)
    heap.insert(4)
    heap.insert(8)
    heap.insert(10)
    print(heap.heap)
    print(len(heap))
