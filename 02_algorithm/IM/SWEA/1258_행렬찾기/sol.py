import sys
sys.stdin = open('input.txt')

# 오른쪽 확인
def check_right(x, y):
    for ny in range(y, N):
        if arr[x][ny] == 0:
            return ny-1
    else:
        return N-1

def check_below(x, y):
    for nx in range(x, N):
        if arr[nx][y] == 0:
            return nx-1
    else:
        return N-1

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    submat = [] # (행길이, 열길이) => nx-x, ny-y

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                ni = check_below(i, j)
                nj = check_right(i, j)
                for k in range(i, ni+1):
                    for l in range(j, nj+1):
                        arr[k][l] = 0
                submat.append([ni-i+1, nj-j+1])

    sorted_submat = sorted(submat, key=lambda x: (x[0]*x[1], x[0]))

    print(f'#{test_case} {len(sorted_submat)}', end=' ')
    for sub in sorted_submat:
        print(*sub, end=' ')
    print()