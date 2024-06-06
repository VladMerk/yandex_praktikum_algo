def max_profit(prices: list) -> int:
    total_profit: int = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            total_profit += prices[i] - prices[i - 1]

    return total_profit


# Чтение входных данных
n = int(input())
prices = list(map(int, input().split()))

# Вычисление и вывод максимальной прибыли
print(max_profit(prices))
