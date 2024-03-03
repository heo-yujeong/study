import sys
sys.stdin = open('input.txt')
from itertools import combinations

T = int(input())

for test_case in range(1, T+1):
    N, L = map(int, input().split())
    TK = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0

    for i in range(1, N+1):
        for comb in combinations(TK, i):
            kcal = 0
            score = 0
            for c in range(len(comb)):
                kcal += comb[c][1]
                score += comb[c][0]
            if kcal > L:
                continue
            if max_score < score:
                max_score = score

    print(f'#{test_case} {max_score}')