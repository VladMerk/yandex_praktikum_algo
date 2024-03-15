"""
Посылка: https://contest.yandex.ru/contest/22781/run-report/109746764/
"""

eval_func = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: x // y}


def postfix_calculator(expression: str) -> int:
    stack = []
    for char in expression.split():
        if char not in "+-*/":
            stack.append(int(char))
        else:
            num_2: int = stack.pop()
            num_1: int = stack.pop()
            stack.append(eval_func[char](num_1, num_2))

    return int(stack.pop())


def main():
    expression = input()
    print(postfix_calculator(expression))


if __name__ == "__main__":
    main()
