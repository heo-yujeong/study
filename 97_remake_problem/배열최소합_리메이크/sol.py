import sys
sys.stdin = open('input.txt')

def backtrack(line, max_line, result, hap):
    global min_hap
    if line == max_line:
        if min_hap > hap:
            min_hap = hap
    elif hap > min_hap:
        return
    else:
        for i in range(N):
            if line_check[i] < 2:
                line_check[i] += 1
                backtrack(line+1, max_line, result + [arr[line][i]],hap+arr[line][i])
                line_check[i] -= 1

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    line_check = [0] * N

    min_hap = N * 100

    backtrack(0, N, [], 0)
    print(f'#{tc} {min_hap}')