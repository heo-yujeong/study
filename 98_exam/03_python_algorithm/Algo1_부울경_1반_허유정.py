import sys
sys.stdin = open('algo1_sample_in.txt')

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # 과녁의 크기
    N = int(input())
    # N * N 과녁 => 점수
    aij = [list(map(int, input().split())) for _ in range(N)]

    # 보너스 점수의 최댓값을 저장할 변수 초기화
    max_score = 0

    # 상하좌우 탐색
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    # 과녁의 모든 지점을 순회
    for i in range(N):
        for j in range(N):
            # 과녁의 한 지점을 맞췄을 때의 점수로 초기화
            score = aij[i][j]
            # 4방향 탐색을 하면서
            for k in range(4):
                # 상하좌우 두칸까지 보너스 점수에 포함
                for l in range(1, 3):
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    # 상하좌우 2칸까지 과녁 범위내에 있다면
                    if 0 <= ni < N and 0 <= nj < N:
                        # 보너스 점수로 합쳐줌
                        score += aij[ni][nj]
            # 보너스 점수 계산이 끝난 후 최댓값과 비교
            # 최댓값보다 현재 계산한 보너스 점수가 더 크다면 값을 바꿔줌
            if max_score < score:
                max_score = score

    print(f'#{test_case} {max_score}')