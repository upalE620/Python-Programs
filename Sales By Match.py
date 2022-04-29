def sockMerchant(n, ar):
    # Write your code here
    l1 = [0] * 101
    for i in ar:
        l1[i] += 1
    l2 = [x // 2 for x in l1 if x > 1]
    return sum(l2)


# 10 20 20 10 10 30 50 10 20

if __name__ == '__main__':
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    print(sockMerchant(n, ar))
