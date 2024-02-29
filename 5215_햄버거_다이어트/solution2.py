import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, L = map(int, input().split())
    TK = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    TK.sort(key=lambda x:x[0], reverse=True)
    print(TK)

    print(f'#{test_case} {max_score}')