def breakingRecords(scores):
    min, max = scores[0], scores[0]
    maxc, minc = 0, 0
    for i in scores:
        if not min <= i <= max:
            if i > max:
                max = i
                maxc += 1
            else:
                min = i
                minc += 1

    return str(maxc),str(minc)


if __name__ == '__main__':
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    print(breakingRecords(scores))
