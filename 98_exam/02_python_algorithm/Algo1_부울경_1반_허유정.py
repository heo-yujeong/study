# import sys
# sys.stdin = open('algo1_sample_in.txt')

T = int(input()) # 테스트 케이스

for test_case in range(1, T+1):
    N = int(input()) # N * N 크기의 칸
    aij = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우를 확인
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 보너스 점수의 최대값을 출력할 변수
    result = 0

    # N * N 칸을 모두 순회하는 동안
    for i in range(N):
        for j in range(N):
            # 마지막에 해당 칸의 점수를 빼기 때문에 해당 칸의 점수를 뺀 값으로 초기화
            hap = -aij[i][j]

            # 네 방향을 검사하면서
            cnt = 0 # 네 방향의 값이 모두 있는지 판단
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                # 해당 칸을 기준으로 상하좌우 값이 존재하면 보너스 점수를 더해줌!
                # 값이 존재하면 cnt에 1을 더해줌
                if 0 <= ni < N and 0 <= nj < N:
                    # 상하좌우 값이 양수이면 더하고
                    # 음수이면 0을 더한다(값 변화 없음)
                    if aij[i][j] > 0:
                        hap += aij[ni][nj]
                    cnt += 1

            # 해당 칸을 기준으로 상하좌우 값이 존재하지 않으면 0점
            if cnt != 4:
                hap = 0

            # 네 방향의 값을 합한 값(hap)이 짝수 점이면 * 2
            if hap % 2 == 0:
                hap *= 2

            # 현재 칸에서 상하좌우를 합한 값이 최대값(result)보다 크면 현재 보너스 점수 값으로 바꿔줌
            if hap > result:
                result = hap

    print(f'#{test_case} {result}')