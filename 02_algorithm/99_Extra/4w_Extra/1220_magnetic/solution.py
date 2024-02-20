import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for j in range(N):
        n_plus = []
        for i in range(N):
            if table[i][j] == 1:
                n_plus.append(1)
            elif table[i][j] == 2 and n_plus:
                count += 1
                n_plus = []

    print(f'#{test_case} {count}')