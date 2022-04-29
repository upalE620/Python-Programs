def getTotalX(a, b):
    c = 0
    for i in range(a[-1], b[0] + 1):
        if (all(i % x == 0 for x in a)) and (all(y % i == 0 for y in b)):
            c += 1
    return c


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    print(getTotalX(arr, brr))
