class HashTable:
    def __init__(self):
        self.max_size = 10 ** 5 - 1
        self.items = [[] for _ in range(self.max_size)]

    def get(self, key: int) -> int | None:
        ...

    def put(self, key: int, value: int) -> None:
        ...

    def delete(self, key: int) -> None:
        ...
