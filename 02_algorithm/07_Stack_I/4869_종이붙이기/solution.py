import sys
sys.stdin = open('input.txt')

T = int(input())

def count_case(n):
    global num_of_case
    if n >= 3 and num_of_case[n] == 0:
        num_of_case[n] = count_case(n-2) * 2 + count_case(n-1)
    return num_of_case[n]

for test_case in range(1, T+1):
    N = int(input())
    n = N // 10

    num_of_case = [0] * (n + 1)
    num_of_case[1] = 1 # 길이가 10일때 경우의 수는 1가지
    num_of_case[2] = 3 # 길이가 20일때 경우의 수는 3가지

    result = count_case(n)

    print(f'#{test_case} {result}')