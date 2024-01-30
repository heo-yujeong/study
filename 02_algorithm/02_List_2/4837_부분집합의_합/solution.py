import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    A = [i for i in range(1, 13)]

    result = [] # 부분집합
    count = 0

    for i in range(1 << len(A)):
        subset = []
        for j in range(len(A)):
            if i & (1 << j):
                subset.append(A[j])
        result.append(subset)

    for i in range(len(result)):
        sum_sub = 0
        if len(result[i]) == N:
            for j in range(N):
                sum_sub += result[i][j]
            if sum_sub == K:
                count += 1

    print(f'#{test_case} {count}')
