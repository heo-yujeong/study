import sys
sys.stdin = open('input.txt')

board = [[0]*1001 for _ in range(1001)]
N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
counts = []

for _ in range(len(papers)):
    x, y, d, r = papers.pop()
    cnt = 0
    for i in range(x, x+d):
        for j in range(y, y+r):
            if board[i][j] == 0:
                board[i][j] = 1
                cnt += 1
    counts.insert(0, cnt)

print(*counts, sep='\n')

# 53점