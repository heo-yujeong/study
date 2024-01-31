import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    A = [i for i in range(1, 13)]

    result = [] # 부분집합 담을 리스트
    count = 0

    for i in range(1 << len(A)):
        subset = [] # i 마다의 부분집합
        for j in range(len(A)):
            if i & (1 << j): # i의 j번째 비트가 1인 경우(j번째 비트가 부분집합에 포함된 경우)
                subset.append(A[j]) # j번 원소를 부분집합에 추가
        result.append(subset) # 완성된 i의 부분집합을 result에 추가

    for i in range(len(result)):
        sum_sub = 0
        if len(result[i]) == N:
            for j in range(N):
                sum_sub += result[i][j]
            if sum_sub == K:
                count += 1

    print(f'#{test_case} {count}')