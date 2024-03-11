eval_func = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: x // y}


def postfix_calculator(expression: str) -> int:
    stack = []
    for char in expression.split():
        if char not in "+-*/":
            stack.append(char)
        else:
            num_2 = stack.pop()
            num_1 = stack.pop()
            stack.append(eval_func[char](int(num_1), int(num_2)))

    return int(stack.pop())


if __name__ == "__main__":
    expression = input()
    print(postfix_calculator(expression))
