import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = float(input())
    result = ''

    for under_dot in range(-1, -14, -1):
        result += str(int(N // (2 ** under_dot)))
        N %= (2 ** under_dot)
        if N == 0:
            break
    else:
        result = 'overflow'

    print(f'#{test_case} {result}')