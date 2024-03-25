# import sys
# sys.stdin = open('algo2_sample_in.txt')

def select(cnt, hap, lst):
    global min_fee
    global max_cnt
    # 건설비의 합계가 예산보다 커지면 return
    # 더 이상 고려할 필요 없음
    if hap > V:
        return

    # 모든 다리 건설을 다 검토 했을 때
    if cnt == N:
        # 건설할 다리의 개수가 최대의 개수라면
        if max_cnt <= len(lst):
            # 최대 다리 개수를 저장하고
            max_cnt = len(lst)
            # 최소 건설 비용 저장
            # 최대 다리 개수가 같다면 건설비용이 적은 값으로 택함
            min_fee = min(min_fee, hap)
        return

    # 해당 다리를 건설하기로 결정했을 경우
    select(cnt+1, hap+Ci[cnt], lst+[Ci[cnt]])
    # 해당 다리를 건설하지 않기로 결정했을 경우
    select(cnt+1, hap, lst)

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # N: 섬의 수, V: 예산
    N, V = map(int, input().split())
    # 각 다리에 대한 건설 비용
    Ci = list(map(int, input().split()))

    # 건설 가능한 최대 다리 개수 초기화
    max_cnt = 0
    # 최소 건설비 초기화
    # 각 다리에 대한 건설비용의 최대값 1000보다 1 큰 값
    #   * 최대로 건설할 수 있는 다리의 개수 N의 값으로 초기화
    min_fee = 1001 * N

    select(0, 0, [])

    print(f'#{test_case} {max_cnt} {min_fee}')