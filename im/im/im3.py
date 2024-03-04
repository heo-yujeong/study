import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M1, M2 = map(int, input().split())
    block = list(map(int, input().split()))
    block.sort()
    weight = 0

    m1 = []
    m2 = []
    for i in range(N):
        if len(m1) < M1:
            m1.append(block.pop())
        if len(m2) < M2:
            m2.append(block.pop())

    for i in range(len(m1)):
        weight += ((i+1) * m1[i])

    for i in range(len(m2)):
        weight += ((i+1) * m2[i])

    print(f'#{tc} {weight}')