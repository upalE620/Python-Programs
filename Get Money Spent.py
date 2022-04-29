def getMoneySpent(keyboards, drives, b):
    l = [x + y for x in keyboards for y in drives if x + y <= b]
    l.sort(reverse=True)
    if not l:
        return -1
    return l[0]


if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))

    print(getMoneySpent(keyboards, drives, b))
