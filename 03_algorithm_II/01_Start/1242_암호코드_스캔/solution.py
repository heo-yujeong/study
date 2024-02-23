import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input().strip()) for _ in range(N)]
    # 모든 수가 0인 라인을 지워줌!
    arr = sorted(arr)[1:]

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] = bin(int(arr[i][j], base=16))[2:].zfill(4)
    for i in range(len(arr)):
        line = ''
        for j in arr[i]:
            line += j
        arr[i] = line
    print(arr)
    password = []
    ct = 0

