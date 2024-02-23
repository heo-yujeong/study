import sys
sys.stdin = open('input.txt')

def backtrack(line, max_line, hap):
    global min_hap
    if line == max_line:
        if min_hap > hap:
            min_hap = hap
    elif min_hap < hap:
        return
    else:
        for i in range(N):
            if line in spc_line:
                backtrack(line + 1, max_line, hap + arr[line][i])
            else:
                if not line_check[i]:
                    line_check[i] = 1
                    backtrack(line + 1, max_line, hap + arr[line][i])
                    line_check[i] = 0

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    spc_line = list(map(int, input().split()))
    for i in range(len(spc_line)): # 인덱스로 쓰게..
        spc_line[i] -= 1
    arr = [list(map(int, input().split())) for _ in range(N)]
    line_check = [0] * N

    min_hap = N * 10

    backtrack(0, N, 0)

    print(f'#{tc} {min_hap}')