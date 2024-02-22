import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, number_16 = input().split()
    number_10 = int(number_16, 16)

    number_2 = format(number_10, 'b')
    if len(number_2) < int(N)*4:
        number_2 = '0' + number_2

    print(f'#{test_case} {number_2}')