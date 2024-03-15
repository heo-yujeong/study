import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            first = honey[i][j:j+M]
            print(first)
