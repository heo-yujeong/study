import sys
sys.stdin = open('input3.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 집 개수
    dist_dict = {}
    dist_lst = []
    for i in range(1, N+1):
        x, y, dist = map(int, input().split())
        dist_lst.append([x, y])
        if dist_dict.get((x, y), 0) != 0:
            dist_dict[(x, y)].append(i)
        else:
            dist_dict[(x, y)] = [i]
        for j in range(4):
            for k in range(1, dist+1):
                nx = x + dx[j]*k
                ny = y + dy[j]*k
                if -15 <= nx <= 15 and -15 <= ny <= 15:
                    if dist_dict.get((nx, ny), 0) != 0:
                        dist_dict[(nx, ny)].append(i)
                    else:
                        dist_dict[(nx, ny)] = [i]

    print(dist_dict)
    result = -1

    for x1, y1 in dist_dict:
        for x2, y2 in dist_dict:
            if (x1, y1) != (x2, y2):
                temp = 0
                charge_albe = []
                charge_albe.extend(*[dist_dict[(x1, y1)]])
                charge_albe.extend(*[dist_dict[(x2, y2)]])
                charge_albe = set(charge_albe)
                if len(charge_albe) == N:
                    for k in range(N):
                        if k+1 in dist_dict[(x1, y1)] and k+1 in dist_dict[(x2, y2)]:
                            temp += min(abs(dist_lst[k][0] - x1) + abs(dist_lst[k][1] - y1), abs(dist_lst[k][0] - x2) + abs(dist_lst[k][1] - y2))
                        elif k+1 in dist_dict[(x1, y1)]:
                            temp += (abs(dist_lst[k][0] - x1) + abs(dist_lst[k][1] - y1))
                        else:
                            temp += (abs(dist_lst[k][0] - x1) + abs(dist_lst[k][1] - y1))
                    result = temp

    for i in dist_dict:
        temp = 0
        if len(dist_dict[i]) == N:
            for j in range(N):
                dist = abs(dist_lst[j][0] - i[0]) + abs(dist_lst[j][1] - i[1])
                temp += dist
            result = temp
    print(f'#{tc} {result}')