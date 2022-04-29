def miniMaxSum(arr):
    print(f"{sum(sorted(arr)[:4])} {sum(sorted(arr)[1:])}")


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
