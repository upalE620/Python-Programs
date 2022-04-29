n = int(input())
arr = map(int, input().split())
l = list(arr)
print(l)
l.sort(reverse=True)
print(l)
a = l[0]
print(a)
l.pop(0)
print(l)
for x in l:
    if x < a:
        print(x)
        break

