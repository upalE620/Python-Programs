
def count_substring(string, sub_string):
    c = 0
    l = []
    for i in range(len(string) + 1 - len(sub_string)):
        s = string[i:i + len(sub_string)]
        l.append(s)
    for j in l:
        if sub_string in j:
            c += 1
    return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)