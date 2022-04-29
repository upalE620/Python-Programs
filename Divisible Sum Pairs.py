def divisibleSumPairs(n, k, ar):
    c = 0
    for i in range(len(ar)):
        for j in range(i + 1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                c += 1
    return c


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])  # 6

    k = int(first_multiple_input[1])  # 3

    ar = list(map(int, input().rstrip().split()))  # [1, 3, 2, 6, 1, 2]

    print(divisibleSumPairs(n, k, ar))
