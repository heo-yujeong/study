import sys
sys.stdin = open('input.txt')

for _ in range(10):
    test_case = int(input())
    mat = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    current = [99, 0]
    for i in range(102):
        if mat[current[0]][i] == 2:
            current[1] = i

    d0 = [-1, 0, 0] # 위왼오
    d1 = [0, -1, 1]
    idx = 0 # 위 : 0, 왼 : 1, 오 : 2

    while current[0] > 0:
        if mat[current[0]][current[1]-1] == 1: # 왼쪽 이동
            idx = 1
            while mat[current[0]][current[1]-1] == 1:
                current[0] += d0[idx]
                current[1] += d1[idx]
            current[0] -= 1

        elif mat[current[0]][current[1]+1] == 1: # 오른쪽 이동
            idx = 2
            while mat[current[0]][current[1]+1] == 1:
                current[0] += d0[idx]
                current[1] += d1[idx]
            current[0] -= 1

        else: # 위로 이동
            idx = 0
            current[0] += d0[idx]

    print(f'#{test_case} {current[1] - 1}')