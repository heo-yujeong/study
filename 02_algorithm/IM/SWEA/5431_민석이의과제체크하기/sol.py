import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    complete = list(map(int, input().split()))

    stu_num = list(range(1, N+1))
    for com in complete:
        stu_num[com-1] = 0

    print(f'#{test_case}', end=' ')
    for stu in stu_num:
        if stu != 0:
            print(stu, end=' ')
    print()