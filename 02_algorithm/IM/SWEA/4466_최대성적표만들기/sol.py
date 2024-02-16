import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)

    total = 0

    for i in range(K):
        total += scores[i]

    print(f'#{test_case} {total}')