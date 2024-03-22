def buble_sort(arr: list):
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if swapped:
            print(*arr, sep=" ")
        else:
            return


def read_input():
    n = int(input())
    arr = list(map(int, input().split()))

    return n, arr


def main():
    n, arr = read_input()
    buble_sort(arr=arr)


if __name__ == "__main__":
    main()
