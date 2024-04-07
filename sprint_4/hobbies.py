def hobbies(n: int):
    d = dict()
    while n > 0:
        name = input()
        if name in d:
            n -= 1
            continue
        else:
            print(name)
            d[name] = 1

        n -= 1


if __name__ == "__main__":
    n = int(input())
    hobbies(n)
