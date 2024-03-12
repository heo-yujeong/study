import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    non_act = {}
    for i in range(N):
        for j in range(M):
            if grid[i][j] > 0:
                non_act[(i, j)] = [grid[i][j], 0]
    act = {}
    dead = set()

    time = 1
    while True:
        act_lst = []
        for y, x in non_act.keys():
            non_act[(y, x)][1] += 1
            if non_act[(y, x)][1] == non_act[(y, x)][0]:
                act[(y, x)] = [non_act[(y, x)][0], 0]
                act_lst.append((y, x))
        for v in act_lst:
            del non_act[v]

        dead_lst = []
        plus = {}
        for y, x in act.keys():
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (ny, nx) not in non_act and (ny, nx) not in act and (ny, nx) not in dead:
                    if plus.get((ny, nx), None) == None:
                        plus[(ny, nx)] = [act[(y, x)][0]]
                    else:
                        plus[(ny, nx)].append(act[(y, x)][0])
            act[(y, x)][1] += 1
            if act[(y, x)][1] == act[(y, x)][0]:
                dead.add((y, x))
                dead_lst.append((y, x))
        for v in dead_lst:
            del act[v]

        for y, x in plus:
            non_act[(y, x)] = [max(plus[(y, x)]), -1]

        time += 1
        if time == K:
            break

    print(f'#{test_case} {len(non_act) + len(act)}')