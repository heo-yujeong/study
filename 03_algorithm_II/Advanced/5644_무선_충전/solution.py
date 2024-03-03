import sys
sys.stdin = open('input.txt')

# X 상 우 하 좌
dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]

T = int(input())

for test_case in range(1, T+1):
    M, A = map(int, input().split())
    A_move = list(map(int, input().split()))
    B_move = list(map(int, input().split()))

    A_loc = (1, 1)
    B_loc = (10, 10)

    able_charge = {}
    for idx in range(1, A+1):
        X, Y, C, P = map(int, input().split())
        for x in range(X-C, X+C+1):
            for y in range(Y-C, Y+C+1):
                if 1 <= x <= 10 and 1 <= y <= 10 and abs(x-X) + abs(y-Y) <= C:
                    if able_charge.get((x, y), 0) != 0:
                        able_charge[(x, y)].append((idx, P))
                    else:
                        able_charge[(x, y)] = [(idx, P)]

    for (x, y) in able_charge:
        if len(able_charge[(x, y)]) >= 2:
            able_charge[(x, y)].sort(key=lambda x:-x[1])

    max_charge = 0
    move_time = 0
    while move_time <= M:
        if A_loc == B_loc:
            if A_loc in able_charge:
                if len(able_charge[A_loc]) >= 2:
                    max_charge += able_charge[A_loc][0][1] + able_charge[A_loc][1][1]
                else:
                    max_charge += able_charge[A_loc][0][1]

        else:
            if A_loc in able_charge and B_loc not in able_charge:
                max_charge += able_charge[A_loc][0][1]
            elif A_loc not in able_charge and B_loc in able_charge:
                max_charge += able_charge[B_loc][0][1]
            elif A_loc in able_charge and B_loc in able_charge:
                if len(able_charge[A_loc]) == len(able_charge[B_loc]) == 1 and able_charge[A_loc][0][0] == able_charge[B_loc][0][0]:
                    max_charge += able_charge[A_loc][0][1]
                elif len(able_charge[A_loc]) >= 2 and len(able_charge[B_loc]) == 1 and able_charge[A_loc][0][0] == able_charge[B_loc][0][0]:
                    max_charge += (able_charge[A_loc][1][1] + able_charge[B_loc][0][1])
                elif len(able_charge[A_loc]) == 1 and len(able_charge[B_loc]) >= 2 and able_charge[A_loc][0][0] == able_charge[B_loc][0][0]:
                    max_charge += (able_charge[A_loc][0][1] + able_charge[B_loc][1][1])
                elif len(able_charge[A_loc]) >= 2 and len(able_charge[B_loc]) >= 2 and able_charge[A_loc][0][0] == able_charge[B_loc][0][0]:
                    max_charge += max(able_charge[A_loc][0][1] + able_charge[A_loc][1][1], able_charge[B_loc][0][1] + able_charge[B_loc][1][1])
                else:
                    max_charge += (able_charge[A_loc][0][1] + able_charge[B_loc][0][1])

        if move_time == M:
            break

        A_loc = (A_loc[0] + dx[A_move[move_time]], A_loc[1] + dy[A_move[move_time]])
        B_loc = (B_loc[0] + dx[B_move[move_time]], B_loc[1] + dy[B_move[move_time]])
        move_time += 1

    print(f'#{test_case} {max_charge}')