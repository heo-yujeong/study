import sys
sys.stdin = open('input.txt')

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    microbe = [] # 세로, 가로, 미생물수, 방향
    for _ in range(K):
        microbe.append(list(map(int, input().split())))

    time = 0
    while True:
        time += 1
        for mic in microbe:
            if mic[2] == 0:
                continue
            mic[0] += dx[mic[3]]
            mic[1] += dy[mic[3]]
            if mic[0] in [0, N-1] or mic[1] in [0, N-1]:
                mic[2] //= 2
                if mic[3] == 1:
                    mic[3] = 2
                elif mic[3] == 2:
                    mic[3] = 1
                elif mic[3] == 3:
                    mic[3] = 4
                else:
                    mic[3] = 3

        plus_dict = {}
        for i in range(len(microbe)-1):
            if microbe[i][2] == 0:
                continue
            plus_list = [microbe[i]]
            for j in range(i+1, len(microbe)):
                if (microbe[i][0], microbe[i][1]) == (microbe[j][0], microbe[j][1]):
                    plus_list.append(microbe[j])
            if len(plus_list) >= 2 and plus_dict.get((microbe[i][0], microbe[i][1]), None) == None:
                plus_dict[(microbe[i][0], microbe[i][1])] = plus_list

        if plus_dict != {}:
            for key, val in plus_dict.items():
                temp = [key[0], key[1]]
                num = 0
                max_num = 0
                for v in val:
                    num += v[2]
                    if max_num < v[2]:
                        max_num = v[2]
                        dir = v[3]
                    v[2] = 0
                temp.append(num)
                temp.append(dir)
                microbe.append(temp)
        if time == M:
            break

    hap = 0
    for mic in microbe:
        hap += mic[2]

    print(f'#{test_case} {hap}')