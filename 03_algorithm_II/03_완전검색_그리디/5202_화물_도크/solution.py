import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    apply = [list(map(int, input().split())) for _ in range(N)]
    apply.sort(key=lambda x: (x[1], x[0]))

    cnt = 0
    pre_end = 0

    for start, end in apply:
        if pre_end <= start:
            pre_end = end
            cnt += 1

    print(f'#{test_case} {cnt}')