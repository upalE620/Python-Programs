# from collections import OrderedDict

def merge_the_tools(string, k):
    i = 0
    l = []
    while i < len(string):
        l.append(string[i:i + k])
        i += k
    for x in l:
        print("".join(dict.fromkeys(x)))



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
