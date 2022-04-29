from itertools import permutations

m, n = input().split()
for i in list(permutations(sorted(m), int(n))):
    print("".join(i))
