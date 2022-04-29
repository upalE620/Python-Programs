
def climbingLeaderboard(ranked, player):
    # Write your code here
    a = sorted(set(ranked),reverse=True)
    b = [] # 6
    for i in player:
        a.append(i)
        a.sort(reverse=True)
        b.append(a.index(i) + 1)
        a.remove(i)
    return a,b



if __name__ == '__main__':


    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    print(climbingLeaderboard(ranked, player))


