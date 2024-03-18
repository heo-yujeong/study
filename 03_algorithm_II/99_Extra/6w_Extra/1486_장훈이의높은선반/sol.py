import sys
sys.stdin = open('input.txt')
from itertools import combinations

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # N: 점원 수, B: 목표 선반 높이
    N, B = map(int, input().split())
    # 직원들의 키
    Hi = list(map(int, input().split()))

    # 가장 작은 높이 차 = 가장 높은 직원 키로 초기화
    min_height = max(Hi)

    # 조합의 개수는 1~N개!
    for i in range(1, N+1):
        comb = list(combinations(Hi, i))
        for j in range(len(comb)):
            # 직원들의 키 합계(탑의 높이)
            hap = sum(comb[j])
            # 각 조합을 만들어서 합이 목표 선반 높이보다 크다면
            if hap >= B:
                # 높이 차가 작은 값을 저장
                min_height = min(min_height, abs(hap-B))

    print(f'#{test_case} {min_height}')