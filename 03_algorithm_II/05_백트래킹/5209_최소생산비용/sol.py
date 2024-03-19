import sys
sys.stdin = open('input.txt')

# 생산한 제품, 생산 비용
def backtrack(line, cost):
    global min_cost
    # 모든 제품을 생산했다면
    if line == N:
        # 최솟값으로 저장
        min_cost = min(min_cost, cost)
        return

    # 모든 제품 생산하지 않았는데 이미 최소 생산 비용을 넘었다면
    # 더이상 계산하지 않고 가지치기
    if cost > min_cost:
        return

    # 공장의 개수만큼 순회하면서
    for i in range(N):
        # 해당 공장에서 제품이 생산되지 않았다면
        if not check[i]:
            # 해당 공장에서 생산했음을 체크하고
            check[i] = 1
            # 해당 칸의 비용을 더해 다음 제품 생산으로
            backtrack(line+1, cost+vij[line][i])
            # 함수 실행 끝나면 다른 공장 선택하기 위해
            # 생산 표시 지움
            check[i] = 0

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # 제품 수
    N = int(input())
    # 공장별 생산비용
    vij = [list(map(int, input().split())) for _ in range(N)]
    # 제품 생산 공장 체크할 배열
    check = [0] * N

    # 최소비용 초기화 = 최대 비용 99 * 제품 수
    min_cost = 99 * N
    backtrack(0, 0)

    print(f'#{test_case} {min_cost}')