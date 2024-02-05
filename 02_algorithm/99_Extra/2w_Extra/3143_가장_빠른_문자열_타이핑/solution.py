import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    A, B = input().split()

    result = 0
    # A 문자열안에 B 문자열이 들어 있는 횟수
    cnt = 0
    idx = 0
    while idx < len(A)-len(B)+1:
        if A[idx : idx + len(B)] == B:
            cnt += 1
            idx += len(B)
        else:
            idx += 1
    result = len(A) - (len(B) * cnt) + cnt

    print(f'#{test_case} {result}')