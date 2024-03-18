import sys
sys.stdin = open('input.txt')

def is_able(row):
    cnt = 1
    for i in range(1, N):
        if row[i] == row[i-1]:
            cnt += 1
        elif row[i] - row[i-1] == 1 and cnt >= X:
            cnt = 1
        elif row[i-1] - row[i] == 1 and cnt >= 0:
            cnt = -X + 1
        else:
            return 0
    if cnt >= 0:
        return 1
    return 0

T = int(input())

for test_case in range(1, T+1):
    N, X = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(N)]

    able_cnt = 0
    for i in range(N):
        if is_able(ground[i]):
            able_cnt += 1

    ground_t = list(map(list, zip(*ground)))
    for i in range(N):
        if is_able(ground_t[i]):
            able_cnt += 1

    print(f'#{test_case} {able_cnt}')