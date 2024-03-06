"""
Нужно реализовать класс StackMax, который поддерживает операцию определения максимума среди всех элементов в стеке.
 Класс должен поддерживать операции push(x), где x – целое число, pop() и get_max().

Формат ввода.
В первой строке записано одно число n — количество команд, которое не превосходит 10000.
В следующих n строках идут команды. Команды могут быть следующих видов:

push(x) — добавить число x в стек. Число x не превышает 10^5;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max() нужно напечатать «None», для команды pop() — «error».

Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения.
Если стек пустой, для команды get_max() напечатайте «None».
Если происходит удаление из пустого стека — напечатайте «error».
"""


class StackMax:
    def __init__(self):
        self.items = []
        self.max_value = [None]

    def is_empty(self):
        return len(self.items) == 0

    def push(self, x):
        self.items.append(x)
        if self.max_value[-1] is None or self.max_value[-1] <= x:
            self.max_value.append(x)

    def pop(self):
        if self.is_empty():
            print("error")
            return
        value = self.items.pop()
        if self.max_value[-1] == value:
            self.max_value.pop()

    def get_max(self):
        if self.is_empty():
            print("None")
            return
        print(self.max_value[-1])


def solution(n: int, stack: StackMax):
    command_dict = {"push": stack.push, "pop": stack.pop, "get_max": stack.get_max}
    while n != 0:
        input_command = input()
        if " " in input_command:
            command, value = input_command.split()
            command_dict[command](value)
        else:
            command_dict[input_command]()

        n -= 1


if __name__ == "__main__":
    stack = StackMax()
    n = int(input())
    solution(n, stack)
