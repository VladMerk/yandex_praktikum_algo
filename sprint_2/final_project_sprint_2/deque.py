"""
Посылка: https://contest.yandex.ru/contest/22781/run-report/109360717/
"""


class Deque:
    def __init__(self, n: int):
        self.deque: list[int | None] = [None] * n
        self.head: int = 0
        self.tail: int = 0
        self.max_n: int = n
        self.size: int = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, value: int) -> None:
        if self.size != self.max_n:
            self.deque[self.tail] = value
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            raise ValueError("error")

    def push_front(self, value: int) -> None:
        if self.size != self.max_n:
            self.head = (self.head + self.max_n - 1) % self.max_n
            self.deque[self.head] = value
            self.size += 1
        else:
            raise ValueError("error")

    def pop_back(self) -> int:
        if self.is_empty():
            raise ValueError("error")
        self.tail = (self.tail + self.max_n - 1) % self.max_n
        value = self.deque[self.tail]
        self.size -= 1
        return value

    def pop_front(self) -> int:
        if self.is_empty():
            raise ValueError("error")

        value = self.deque[self.head]
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return value


def get_result_operation(d: Deque, operation: str) -> int | str:
    commands = {
        "push_back": d.push_back,
        "push_front": d.push_front,
        "pop_back": d.pop_back,
        "pop_front": d.pop_front,
    }
    command: list = operation.split()
    try:
        if len(command) > 1:
            return commands[command[0]](int(command[1]))
        else:
            return commands[command[0]]()
    except ValueError as e:
        return str(e)


def main():
    n = int(input())
    m = int(input())

    deque = Deque(m)

    while n > 0:
        result = get_result_operation(deque, input())
        if result is not None:
            print(result)
        n -= 1


if __name__ == "__main__":
    main()
