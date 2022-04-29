l1, l2, l3, l4, lst = [], [], [], [], []

for _ in range(int(input())):
    name = input()
    l1.append(name)
    score = float(input())
    l1.append(score)
    lst.append(l1)
    l1 = []

for x in lst:
    l2.append(x[1])

l2.sort()
l3 = [a for a in l2 if a > l2[0]]

for y in lst:
    if y[1] == l3[0]:
        l4.append(y[0])

l4.sort()

for z in l4:
    print(z)
