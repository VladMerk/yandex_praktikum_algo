"""
Вычисление чисел Фибоначи с обычной рекурсией и через динамическое программирование.
"""


def fibo_rec(n: int) -> int:  # sourcery skip: assign-if-exp, reintroduce-else
    """Решение только через рекурсию."""
    if n <= 1:
        return n

    return fibo_rec(n-1) + fibo_rec(n-2)


def fibo_dp(n: int) -> int:
    if n <= 1:
        return n

    fib: list[int] = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]

    return fib[n]
