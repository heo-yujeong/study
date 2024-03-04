import sys
sys.stdin = open('input3.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    dist_loc = {}  # 원래 위치
    dist_dict = {} # 범위 포함되는 위치
    for i in range(1, N+1):
        X, Y, dist = map(int, input().split())
        dist_loc[i] = [X, Y]
        for x in range(X-dist, X+dist+1):
            for y in range(Y-dist, Y+dist+1):
                if -15 <= x <= 15 and -15 <= y <= 15 and abs(X-x)+abs(Y-y)<=dist and (x != X or y != Y):
                    if dist_dict.get((x, y), 0) != 0:
                        dist_dict[(x, y)].append(i)
                    else:
                        dist_dict[(x, y)] = [i]

    # print(dist_loc)
    # print(dist_dict)
    result = 1e9

    for key, value in dist_dict.items():
        temp = []
        tmp_hap = 0
        if len(value) == N:
            # print(key, value)
            for i in range(1, N+1):
                tmp_hap += (abs(key[0] - dist_loc[i][0]) + abs(key[1] - dist_loc[i][1]))
            temp.append(tmp_hap)

        else:
            for key2, value2 in dist_dict.items():
                if key != key2:
                    tmp_hap = 0
                    if len(set(value+value2)) == N:
                        # print(key, value, key2, value2)
                        for i in range(1, N+1):
                            if i in value and i in value2:
                                tmp_hap += min(abs(key[0] - dist_loc[i][0]) + abs(key[1] - dist_loc[i][1]), abs(key2[0] - dist_loc[i][0]) + abs(key2[1] - dist_loc[i][1]))
                            elif i in value:
                                tmp_hap += (abs(key[0] - dist_loc[i][0]) + abs(key[1] - dist_loc[i][1]))
                            else:
                                tmp_hap += (abs(key2[0] - dist_loc[i][0]) + abs(key2[1] - dist_loc[i][1]))
                        # print(tmp_hap)
                        temp.append(tmp_hap)
                        # print(temp)
        if temp:
            result = min(min(temp), result)

    if result == 1e9:
        result = -1

    print(f'#{tc} {result}')