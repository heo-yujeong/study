import sys
sys.stdin = open('input.txt')

def permut(i, hap):
    global cnt
    if hap == K:
        cnt += 1
        return
    if i == N:
        return
    permut(i+1, hap+A[i])
    permut(i+1, hap)


T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0

    permut(0, 0)

    print(f'#{test_case} {cnt}')