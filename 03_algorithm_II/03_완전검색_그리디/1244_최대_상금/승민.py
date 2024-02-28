import sys

sys.stdin = open('input.txt')


def turn(m):
    global max_num

    if m == M:
        max_num = max(int(''.join(num)), max_num)
        return

    for i in range(num_len - 1):
        for j in range(i + 1, num_len):
            num[i], num[j] = num[j], num[i]
            char = ''.join(num)
            if (m, char) not in visited:
                turn(m + 1)
                visited.append((m, char))
            num[i], num[j] = num[j], num[i]


T = int(input())
# T = 1
for t in range(1, T + 1):
    # N 자리수 1 <= N <= 6, 교환 횟수 M번 1 <= M <= 10
    N, M = map(int, input().split())
    max_num = -1
    num = list(str(N))
    num_len = len(num)
    visited = []
    turn(0)
    print(f'#{t} {max_num}')