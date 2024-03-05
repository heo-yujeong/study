import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    floor = [list(map(int, input().split())) for _ in range(N)]

    stairs = {} # {계단 번호 : [세로위치, 가로위치, 길이]}
    stairs_num = 1
    people_loc = {}  # {번호: [목표 계단, 계단입구 까지의 거리]}
    people_num = 1
    for i in range(N):
        for j in range(N):
            if floor[i][j] >= 2:
                stairs[stairs_num] = [i, j, floor[i][j]]
                stairs_num += 1

    '''
    계단 선택을.... 
    무조건 거리가 짧은 기준이 아니고..
    '''

    for i in range(N):
        for j in range(N):
            if floor[i][j] == 1:
                s1_d = abs(stairs[1][0] - i) + abs(stairs[1][1] -j)
                s2_d = abs(stairs[2][0] - i) + abs(stairs[2][1] -j)
                if s1_d > s2_d:
                    people_loc[people_num] = [2, s2_d]
                else:
                    people_loc[people_num] = [1, s1_d]
                people_num += 1

    arrive_stair = [] # [사람번호, 목표계단, 도착 시간]
    waiting = [[0] * 3 for _ in range(2)]
    time = 1
    while True:
        if len(people_loc) == 0 and (sum(waiting[0])+sum(waiting[1])) == 0 and arrive_stair == []:
            break
        for i in range(1, people_num+1):
            if people_loc.get(i, None) != None:
                people_loc[i][1] -= 1
                if people_loc[i][1] == 0:
                    arrive_stair.append([i, people_loc[i][0], time])
                    del people_loc[i]
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

    print(f'#{test_case} {time}')