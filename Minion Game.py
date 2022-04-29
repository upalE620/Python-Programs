def minion_game(string):
    k, s = 0, 0
    vowel = "AEIOU"
    for i in range(1, len(string) + 1):
        a = 0
        while a + i <= len(string):
            if string[a:a + i][0] in vowel:
                k += 1
            else:
                s += 1
            a += 1
    if k > s:
        print("Kevin", k)
    elif k == s:
        print("Draw")
    else:
        print("Stuart", s)


if __name__ == '__main__':
    s = input()
    minion_game(s)
