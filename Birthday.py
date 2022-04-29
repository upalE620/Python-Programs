def birthday(s, d, m):
    c = 0
    for i in range(len(s)):
        if sum(s[i:i + m]) == d:
            c += 1
    return c


if __name__ == '__main__':
    n = int(input().strip())  # 5

    s = list(map(int, input().rstrip().split()))  # [2,2,1,3,2]

    first_multiple_input = input().rstrip().split()  # 4 2

    d = int(first_multiple_input[0])  # 4

    m = int(first_multiple_input[1])  # 2

    print(birthday(s, d, m))
