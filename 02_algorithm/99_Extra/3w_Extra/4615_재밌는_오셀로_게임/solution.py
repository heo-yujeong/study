import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    board[N//2-1][N//2] = board[N//2][N//2-1] = 1 # 1 = 흑돌
    board[N//2][N//2] = board[N//2-1][N//2-1] = 2 # 2 = 백돌

    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]

    for _ in range(M):
        x, y, color = map(int, input().split())
        x, y = x-1, y-1

