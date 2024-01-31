import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, Q = map(int, input().split()) # N : 상자 개수, Q : 반복 횟수

    result = [0] * (N+1)

    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            result[j] = i+1

    print(f'#{test_case}', *result[1:])