import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    str1 = input()
    str2 = input()

    is_sub = 0

    if str1 in str2:
        is_sub = 1

    print(f'#{test_case} {is_sub}')