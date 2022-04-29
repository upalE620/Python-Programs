#!/bin/python3


# Complete the solve function below.
def solve(s):
    return " ".join([x[0].upper() + x[1:] for x in s.split()])


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
