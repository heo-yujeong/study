import sys
sys.stdin = open('input.txt')
from itertools import product

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    floor = [list(map(int, input().split())) for _ in range(N)]

    stairs = {} # {계단 번호 : [세로위치, 가로위치, 길이]}
    stairs_num = 1
    people_loc = {}  # {번호: [1번 계단 시간, 2번 계단 시간]}
    people_num = 1
    for i in range(N):
        for j in range(N):
            if floor[i][j] >= 2:
                stairs[stairs_num] = [i, j, floor[i][j]]
                stairs_num += 1

    for i in range(N):
        for j in range(N):
            if floor[i][j] == 1:
                s1_d = abs(stairs[1][0] - i) + abs(stairs[1][1] -j)
                s2_d = abs(stairs[2][0] - i) + abs(stairs[2][1] -j)
                people_loc[people_num] = [s1_d, s2_d]
                people_num += 1

    min_time = []
    select_stair = {} # {번호: [목표 계단, 계단입구 까지의 거리]}
    for stair in list(product([1, 2], repeat=len(people_loc))):
        for num in people_loc.keys():
            if stair[num-1] == 1:
                select_stair[num] = [1, people_loc[num][0]]
            elif stair[num-1] == 2:
                select_stair[num] = [2, people_loc[num][1]]

        arrive_stair = [] # [사람번호, 목표계단, 도착 시간]
        waiting = [[0] * 3 for _ in range(2)]
        time = 1
        while True:
            if len(select_stair) == 0 and (sum(waiting[0])+sum(waiting[1])) == 0 and arrive_stair == []:
                break
            for i in range(1, people_num+1):
                if select_stair.get(i, None) != None:
                    select_stair[i][1] -= 1
                    if select_stair[i][1] == 0:
                        arrive_stair.append([i, select_stair[i][0], time])
                        del select_stair[i]
            for i in range(2):
                for j in range(3):
                    waiting[i][j] -= 1
                    if waiting[i][j] < 0:
                        waiting[i][j] = 0

            time += 1
            if arrive_stair:
                for _ in range(len(arrive_stair)):
                    if arrive_stair[0][2] < time and 0 in waiting[arrive_stair[0][1]-1]:
                        pn, gsn, t = arrive_stair.pop(0)
                        waiting[gsn-1][waiting[gsn-1].index(0)] = stairs[gsn][2]
        min_time.append(time)

    print(f'#{test_case} {min(min_time)}')