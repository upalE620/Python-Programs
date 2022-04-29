x = int(input())  # 1
y = int(input())  # 2
z = int(input())  # 3
n = int(input())
l1 = []
l2 = []
for a in range(x + 1):
    for b in range(y + 1):
        for c in range(z + 1):
            l2 = [a, b, c]
            l1.append(l2)

l = [d for d in l1 if d[0] + d[1] + d[2] != n]
print(l)
