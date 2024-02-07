import sys
sys.stdin = open('input.txt')

T = int(input())

def count_case(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n >= 3:
        return count_case(n-2) * 2 + count_case(n-1)

for test_case in range(1, T+1):
    N = int(input())
    n = N // 10

    result = count_case(n)

    print(f'#{test_case} {result}')