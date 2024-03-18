import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def backtrack(cnt, y, x, str_num):
    if cnt == 7:
        result.add(str_num)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            backtrack(cnt+1, ny, nx, str_num+str(board[ny][nx]))

T = int(input())

for test_case in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(4)]

    result = set()
    for i in range(4):
        for j in range(4):
            backtrack(1, i, j, str(board[i][j]))

    print(f'#{test_case} {len(result)}')