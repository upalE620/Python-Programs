
def formingMagicSquare(s):
    # Write your code here
    l = []
    for i in s:
        for j in i:
            l.append(j)


    possibilities = []
    for a in range(1, 10):
        for b in range(1, 10):
            if set([a, 15 - a - b, b, 5 + b - a, 5, 5 + a - b, 10 - b, a + b - 5, 10 - a]) == set(range(1, 10)):
                possibilities.append([a, 15 - a - b, b,
                                      5 + b - a, 5, 5 + a - b,
                                      10 - b, a + b - 5, 10 - a])

    minCost = 100
    for possibility in possibilities:
        cost = 0
        for i in range(9):
            cost += abs(l[i] - possibility[i])
        if cost < minCost:
            minCost = cost
    return minCost

if __name__ == '__main__':


    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    print(formingMagicSquare(s))


