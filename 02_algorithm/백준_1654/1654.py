import sys
sys.stdin = open('input.txt')

# K: 랜선 개수, N: 잘라서 만들 랜선 개수
K, N = map(int, input().split())
# 각 랜선의 길이
bar = [int(input()) for _ in range(K)]

# 랜선 길이 최소
min_len = 1
# 랜선 길이 최대
max_len = max(bar)

# 이진탐색 => 최소값이 최대값보다 작을 때까지 반복
while min_len <= max_len:
    # 중간 값 = (최소 + 최대) // 2
    center_len = (min_len + max_len) // 2

    # 자른 전선 개수
    sun_cnt = 0
    # 랜선을 하나씩 순회하면서
    for b in bar:
        # 랜선을 중간 값으로 나눈 몫들의 합 = 자른 랜선의 개수
        sun_cnt += b // center_len
    
    # 자른 랜선의 개수가 목표치보다 작으면
    # 너무 큰 길이로 잘라져서 목표를 달성하지 못했다
    if sun_cnt < N:
        # 길이를 짧게 주기 위해 최대값을 중간값보다 1 작게
        max_len = center_len -1
    # 자른 랜선의 개수가 목표치보다 크면
    else:
        # 길이를 길게 주기 위해 최소값을 중간값보다 1 크게
        min_len = center_len + 1

# 위 과정을 모두 순회한 결과의 랜선 길이 최대
print(max_len)