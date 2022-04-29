import string

a = string.ascii_lowercase
L = []


def print_rangoli():
    # your code goes here
    # 4n - 3
    for i in range(n):
        s = "-".join(a[i:n])
        L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
    print('\n'.join(L[:0:-1] + L))


if __name__ == '__main__':
    n = int(input())
    print_rangoli()
