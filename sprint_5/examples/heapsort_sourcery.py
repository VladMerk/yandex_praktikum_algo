from dataclasses import dataclass


@dataclass
class User:
    name: str
    tasks: int
    penalty: int

    def __lt__(self, other: "User") -> bool:
        if self.tasks != other.tasks:
            return self.tasks > other.tasks
        elif self.penalty != other.penalty:
            return self.penalty < other.penalty
        else:
            return self.name < other.name

    def __repr__(self) -> str:
        return self.name


def sift_up(arr, index):
    if index == 0:
        return

    parent_index = (index - 1) // 2
    if arr[parent_index] < arr[index]:
        arr[parent_index], arr[index] = arr[index], arr[parent_index]
        sift_up(arr, parent_index)


def sift_down(arr, n, i):
    largest = i
    left = 2 * i + 1
    r = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        sift_down(arr, n, largest)


def heapify(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, n, i)


def heap_sort(arr):
    heapify(arr)
    n = len(arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        sift_down(arr, i, 0)


# Example usage
# users = [User("Alice", 5, 10), User("Bob", 3, 15), User("Charlie", 7, 8)]
users = [User("alla", 4, 100), User("timofey", 4, 80), User("gena", 6, 1000)]
heap_sort(users)
print("Sorted users:")
for user in users:
    print(user)
