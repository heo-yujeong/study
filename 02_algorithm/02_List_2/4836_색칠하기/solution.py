import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    red = [[0] * 10 for _ in range(10)] # 빨간색 칠할 배열
    blue = [[0] * 10 for _ in range(10)] # 파란색 칠할 배열
    purple = [[0] * 10 for _ in range(10)] # 두 배열의 합 = 2 이면 보라색

    N = int(input()) # 색칠 횟수

    for num in range(N):
        colors = list(map(int, input().split())) # 왼쪽 위 인덱스, 오른쪽 아래 인덱스, 색상

        if colors[4] == 1: # 빨간색인 경우
            for i in range(colors[0], colors[2]+1):
                for j in range(colors[1], colors[3]+1):
                    red[i][j] = 1

        else: # 파란색인 경우
            for i in range(colors[0], colors[2]+1):
                for j in range(colors[1], colors[3]+1):
                    blue[i][j] = 1


    result = 0 # 보라색 칸 수 세기
    for i in range(10):
        for j in range(10):
            purple[i][j] = red[i][j] + blue[i][j]
            if purple[i][j] == 2: # 빨간색도 칠해져 있고, 파란색도 칠해져 있으면
                result += 1 # 보라색 칸 수 +1

    print(f'#{test_case} {result}')