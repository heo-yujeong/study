import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    red = [[0] * 10 for _ in range(10)]
    blue = [[0] * 10 for _ in range(10)]
    purple = [[0] * 10 for _ in range(10)]
    N = int(input())
    for num in range(N):
        colors = list(map(int, input().split()))
        if colors[4] == 1:
            for i in range(colors[0], colors[2] + 1):
                for j in range(colors[1], colors[3] + 1):
                    red[i][j] = 1
        else:
            for i in range(colors[0], colors[2] + 1):
                for j in range(colors[1], colors[3] + 1):
                    blue[i][j] = 1

    result = 0
    for i in range(10):
        for j in range(10):
            purple[i][j] = red[i][j] + blue[i][j]
            if purple[i][j] == 2:
                result += 1

    print(f'#{test_case} {result}')