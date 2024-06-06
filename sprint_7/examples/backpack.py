'''
Задача о рюкзаке (Knapsack Problem)
Рассмотрим классическую задачу о рюкзаке, где нужно максимизировать стоимость предметов,
помещенных в рюкзак с ограниченной вместимостью.

Формулировка задачи:
У нас есть рюкзак, который может вместить предметы с общей массой не более 𝑊. У нас есть
n предметов, каждый из которых имеет массу W(i) и стоимость v(i).
Нужно выбрать набор предметов, чтобы максимизировать общую стоимость, не превышая массу W.
'''
import pprint


def knapsack(weights: list, prices: list, W: int) -> int:
    n: int = len(weights)
    dp: list[list[int]] = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + prices[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    pprint.pprint(dp)
    print()
    return dp[n][W]


# Пример использования:
weights: list[int] = [1, 3, 4, 5]
prices: list[int] = [1, 4, 5, 7]
W = 7
print(knapsack(weights, prices, W))  # Вывод: 9
