import sys
sys.stdin = open('input.txt')

for _ in range(10):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = 0
    check = False # 아직 원하는 지점 찾지 못함

    # 사다리 크기 = 100 * 100
    for i in range(100):
        for j in range(100):
            # 출발 지점
            if i == 0 and arr[i][j] == 1:
                visited = [[0] * 100 for _ in range(100)]  # 방문했는지 체크
                original_j = j # 출발 시점의 j 좌표(original_j)
                while i != 99: # 탐색 : x가 99가 될 때까지 순회
                    # 3방향 탐색!
                    for dir in [(1, 0), (0, -1), (0, 1)]: # 아래 왼 오
                        # 다음 탐색 대상의 i, j 좌표값
                        ni = i + dir[0]
                        nj = j + dir[1]
                        if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] == 1: # 이동 가능
                            if not visited[ni][nj]:
                                visited[i][j] = 1 # 방문한적 있음을 표시
                                i, j = ni, nj # 이동
                        if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] == 2:
                            result = original_j
                            check = True
                            break
                    if check: # while문 벗어남
                        break
            if check: # j for문 종료
                break
        if check: # i for문 종료
            break

    print(result)