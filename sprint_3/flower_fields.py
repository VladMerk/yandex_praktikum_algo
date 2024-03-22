def merge_intervals(field: list[list[int]]) -> list[list[int]]:
    field.sort(key=lambda x: x[0])
    merged = [field[0]]
    for interval in field[1:]:
        if interval[0] <= merged[-1][1]:
            merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        else:
            merged.append(interval)

    return merged


def read_input() -> list[list[int]]:
    n = int(input())
    intervals = []
    while n > 0:
        intervals.append(list(map(int, input().split())))
        n -= 1

    return intervals


def main():
    intervals = read_input()
    result = merge_intervals(intervals)
    for item in result:
        print(*item, sep=" ")


if __name__ == "__main__":
    main()
