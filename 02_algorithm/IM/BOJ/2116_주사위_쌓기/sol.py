import sys
sys.stdin = open('input.txt')

N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]

max_hap = 0
under_top = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

for idx in range(6):
    side_hap = []
    lowest_dice = [1, 2, 3, 4, 5, 6]

    under = dice[0][idx]
    top = dice[0][under_top[idx]]

    lowest_dice.remove(under)
    lowest_dice.remove(top)

    side_hap.append(max(lowest_dice))

    for i in range(1, N):
        next_dice = [1, 2, 3, 4, 5, 6]

        under = top
        under_idx = dice[i].index(under)
        top = dice[i][under_top[under_idx]]

        next_dice.remove(under)
        next_dice.remove(top)

        side_hap.append(max(next_dice))

    if max_hap < sum(side_hap):
        max_hap = sum(side_hap)

print(max_hap)