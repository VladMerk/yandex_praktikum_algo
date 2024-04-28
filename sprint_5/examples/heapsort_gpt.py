class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap) - 1
        while i > 0 and self.compare(self.heap[self.parent(i)], self.heap[i]):
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def min_heapify(self, i):
        l = self.left_child(i)
        r = self.right_child(i)
        smallest = i
        if l < len(self.heap) and self.compare(self.heap[l], self.heap[i]):
            smallest = l
        if r < len(self.heap) and self.compare(self.heap[r], self.heap[smallest]):
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min_element = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.min_heapify(0)
        return min_element

    def compare(self, participant1, participant2):
        if participant1[1] != participant2[1]:  # По количеству решенных задач
            return participant1[1] > participant2[1]
        elif participant1[2] != participant2[2]:  # По размеру штрафа
            return participant1[2] > participant2[2]
        else:  # По логину
            return participant1[0] < participant2[0]


def heap_sort(arr):
    heap = MinHeap()
    for element in arr:
        heap.insert(element)
    sorted_arr = []
    for _ in range(len(arr)):
        sorted_arr.append(heap.extract_min())
    return sorted_arr

participants_input = [
    ("alla", 4, 100),
    ("gena", 6, 1000),
    ("gosha", 2, 90),
    ("rita", 2, 90),
    ("timofey", 4, 80)
]

# Сортировка участников с помощью сортировки кучей
sorted_participants = heap_sort(participants_input)

# Вывод отсортированных логинов участников
for participant in sorted_participants:
    print(participant[0])
