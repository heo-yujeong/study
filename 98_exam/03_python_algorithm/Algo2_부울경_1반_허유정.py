import sys
sys.stdin = open('algo2_sample_in.txt')

# 최댓값을 찾는 함수
def chk_max_score(x, y):
    # 시작하는 위치의 값을 최대값으로 초기화
    max_score = aij[x][y]
    # 가장 큰 값일 때의 (x, y)도 해당 위치로 초기화
    max_x = x
    max_y = y
    # M * M 행렬을 순회하면서 (최댓값의 인덱스 ~ 최댓값의 인덱스+ M)
    for i in range(x, x+M):
        for j in range(y, y+M):
            # 해당 위치가 N*N 행렬을 벗어나지 않을 때만 비교
            if 0 <= i < N and 0 <= j < N:
                # 현재 위치의 값이 최댓값보다 크다면 값을 바꿔줌
                # (x, y) 도 해당 위치로 바꿔줌
                if max_score < aij[i][j]:
                    max_score = aij[i][j]
                    max_x = i
                    max_y = j
    # 해당 범위내에서 최댓값을 찾은 후
    # hap 리스트가 비어있지 않고, 함수 시작위치의 좌표와 최댓값의 좌표가 동일하면
    if hap and x == max_x and y == max_y:
        # 최댓값을 더하지 않고 함수 종료
        return
    # hap 리스트가 비어있거나(처음 함수 실행), 시작위치의 좌표와 최댓값의 좌표가 다르면
    else:
        # hap 리스트에 최댓값을 append
        hap.append(max_score)
        # 최댓값을 찾는 함수 다시 호출
        # 그때의 인자는 현재 찾은 최댓값의 (x, y)좌표인 max_x와 max_y
        chk_max_score(max_x, max_y)

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # N: 행렬의 크기, M: 탐색할 행렬의 크기
    N, M = map(int, input().split())
    # N * N 행렬
    aij = [list(map(int, input().split())) for _ in range(N)]

    # M*M 행렬의 최댓값들을 저장할 리스트
    hap = []
    # 최댓값을 찾는 함수 실행
    # 시작은 무조건 (0, 0) 위치
    chk_max_score(0, 0)

    # 결과 = hap 리스트에 있는 모든 값의 합
    print(f'#{test_case} {sum(hap)}')