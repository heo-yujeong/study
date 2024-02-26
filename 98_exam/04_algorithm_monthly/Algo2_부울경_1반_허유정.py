# import sys
# sys.stdin = open('algo2_sample_in.txt')

# 최대 점수를 찾을 함수
# 매개변수
# line : 몇번째 줄까지 조사했는지 체크
# hap : 점수의 합계
# result : 어떤 요소들이 포함되는지
def get_max_score(line, hap, result):
    global max_score
    # 마지막 줄까지 조사를 했다면
    if line == N:
        # 어떤 요소가 포함되었는지 담겨있는 result 리스트를 순회하면서
        # 음수인 점수가 포함되어 있다면 그때의 hap은 0점
        for i in result:
            if i < 0:
                hap = 0
        # 그때의 합과 최대 점수를 비교하여 큰 값을 최대 점수로
        if max_score < hap:
            max_score = hap
    # 마지막 줄까지 조사하지 않았다면
    else:
        # 해당 줄에 있는 모든 요소를 하나씩 더해보면서 체크
        for i in range(N):
            # 해당 열이 포함되지 않았다면
            if not line_chk[i]:
                # 포함 표시를 하고
                line_chk[i] = 1
                # 다음 줄을 조사(hap과 result에 현재 값을 더해서)
                get_max_score(line+1, hap+aij[line][i], result+[aij[line][i]])
                # 조사가 끝나면 포함 표시를 해제
                line_chk[i] = 0

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # 표적의 크기(N*N)
    N = int(input())
    # 점수가 적인 표적
    aij = [list(map(int, input().split())) for _ in range(N)]
    # 세로에 한개씩 선택했는지 체크할 리스트
    line_chk = [0] * N

    # 최대 점수 저장할 변수 초기화
    max_score = 0

    # 최대 점수를 찾을 함수 실행
    get_max_score(0, 0, [])

    print(f'#{test_case} {max_score}')