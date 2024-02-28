import sys
sys.stdin = open('input.txt')

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(1001)] for _ in range(1001)]
count = []

for k in range(N-1, -1, -1) :
    x, y, w, h = arr[k][0], arr[k][1], arr[k][2], arr[k][3]
    sum_num = 0
    for i in range(x, x+w) :
        for j in range(y, y+h) :
            if visited[i][j] == 0:
                visited[i][j] = 1
                sum_num += 1

    count.insert(0, sum_num)
print(*count, sep='\n')