N = int(input())
l = []
for i in range(N):
    s = input()
    if s.startswith("insert"):
        l.insert(int(s.split()[1]), int(s.split()[2]))
    elif s == 'print':
        print(l)
    elif s.startswith("remove"):
        l.remove(int(s.split()[1]))
    elif s.startswith("append"):
        l.append(int(s.split()[1]))
    elif s == 'sort':
        l.sort()
    elif s == 'pop':
        l.pop()
    elif s == 'reverse':
        l.reverse()
    else:
        print("Wrong Command!")
