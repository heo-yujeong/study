import sys
sys.stdin = open('input.txt')

# 사람(직원), 성공할 확률
def backtrack(work, per):
    global max_per
    # 모든 일을 다 배분했다면
    if work == N:
        # 최대 확률 갱신
        max_per = max(max_per, per)
        return
    # 확률에는 음수 값이 없기 때문에(0 ~ 1)
    # 모든 일을 다 배분하지 않았을 때
    # 최대 확률보다 값이 작으면 가지치기
    if max_per >= per:
        return

    # 모든 일을 배분할 때까지 반복
    for i in range(N):
        # 해당 일을 아직 배분하지 않았다면
        if not check[i]:
            # 배분해주고
            check[i] = 1
            # 다음 사람 일 배분하러 감
            # pij 값은 0~100 사이의 정수
            # 확률은 해당 값에 0.01을 곱한 값으로
            backtrack(work+1, per*pij[work][i]*0.01)
            # 함수 실행이 끝나면 다른 사람에게도 해당 일을 배분할 수 있도록
            # 표시 해제
            check[i] = 0

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # 직원 수
    N = int(input())
    # i번 직원이 j번 일을 성공할 확률
    pij = [list(map(int, input().split())) for _ in range(N)]
    # j번 일을 했는지 체크할 배열
    check = [0] * N

    # 최대 확률 초기화
    # 0 ~ 100 사이값이 입력되기 때문에 0으로
    max_per = 0
    backtrack(0, 1)

    # 소수점 아래 6자리 나타냄
    print(f'#{test_case} {max_per*100:.6f}')