import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))

    wi.sort(reverse=True)
    ti.sort(reverse=True)

    move = []

    for t in ti:
        if wi:
            for i in range(len(wi)):
                if t >= wi[i]:
                    move.append(wi[i])
                    wi.remove(wi[i])
                    break

    print(f'#{test_case} {sum(move)}')