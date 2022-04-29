def timeConversion(s):
    # Write your code here
    if s[-2] == 'A':
        if s[:2] == '12':
            return f"00{s[2:-2]}"
        else:
            return s[:-2]
    else:
        if s[:2] != '12':
            return f"{int(s[:2]) + 12}:{s[3:-2]}"
        else:
            return s[:-2]


if __name__ == '__main__':
    s = input()

    result = timeConversion(s)

    print(result)
