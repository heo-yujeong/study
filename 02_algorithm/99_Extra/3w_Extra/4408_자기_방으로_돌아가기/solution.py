import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    corridor = [0] * 201

    for _ in range(N):
        start, end = map(int, input().split())

        start = (start + 1) // 2
        end = (end + 1) // 2

        if start < end:
            for i in range(start, end+1):
                corridor[i] += 1
        else:
            for i in range(end, start+1):
                corridor[i] += 1

    print(f'#{test_case} {max(corridor)}')