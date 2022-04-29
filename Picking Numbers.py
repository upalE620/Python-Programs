def pickingNumbers(a):
    # Write your code here
    a.sort() # 1 3 3 4 5 6
    c = 0
    for i in a:
        l = [x for x in a if abs(i - x) <= 1 and i <= x <= i + 1]
        if len(l) > c:
            c = len(l)
    return c


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    print(pickingNumbers(a))

