import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    wire = []
    cnt = 0

    for _ in range(N):
        a, b = map(int, input().split())
        wire.append([a, b])

    for i in range(N):
        for j in range(i, N):
            if i != j:
                if wire[i][0] > wire[j][0] and wire[i][1] < wire[j][1]:
                    cnt += 1
                elif wire[i][0] < wire[j][0] and wire[i][1] > wire[j][1]:
                    cnt += 1

    print(f'#{test_case} {cnt}')