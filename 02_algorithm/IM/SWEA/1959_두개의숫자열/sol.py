import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))

    max_sum = 0

    if M >= N:
        for i in range(M-N+1):
            hap = 0
            slice_b = arr_b[i:i+N]
            for j in range(N):
                hap += (arr_a[j] * slice_b[j])
            if hap > max_sum:
                max_sum = hap
    else:
        for i in range(N-M+1):
            hap = 0
            slice_a = arr_a[i:i+M]
            for j in range(M):
                hap += (arr_b[j] * slice_a[j])
            if hap > max_sum:
                max_sum = hap

    print(f'#{test_case} {max_sum}')