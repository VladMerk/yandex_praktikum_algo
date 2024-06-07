def can_partition(points: list) -> bool:
    total_sum: int = sum(points)
    if total_sum % 2 != 0:
        return False

    target: int = total_sum // 2
    dp: list[bool] = [False] * (target + 1)
    dp[0] = True

    for point in points:
        for j in range(target, point - 1, -1):
            dp[j] = dp[j] or dp[j - point]

    return dp[target]


n = int(input())
points = list(map(int, input().strip().split()))

print(can_partition(points))
