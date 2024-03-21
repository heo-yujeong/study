import sys
sys.stdin = open('input.txt')

def find_set(x):
    if parents[x] == x:
        return x
    return find_set(parents[x])

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # 섬의 개수
    N = int(input())
    # 각 섬의 x, y 좌표
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    # 환경 부담 세율
    E = float(input())

    # 섬들 간 환경 부담금 계산
    # 출발, 도착, 환경부담금
    edges = []
    for i in range(N):
        for j in range(i+1, N):
            # 환경 부담금 = 환경 부담 세율 * 섬 사이의 거리 **2
            w = ((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) * E
            edges.append([i, j, w])

    # 환경 부담금이 작은 순으로 정렬
    edges.sort(key=lambda x:x[2])

    # 사이클을 제거하기 위한 부모 노드 정의
    parents = [i for i in range(N)]
    # 연산 횟수 줄이기 == N-1 과 같아지면 종료해도 ok
    # = 모든 섬이 연결 되었다는 의미
    cnt = 0
    # 지불할 환경 부담금
    hap_fee = 0

    for s, e, w in edges:
        # 사이클이 발생하면 pass
        if find_set(s) == find_set(e):
            continue
        # 사이클이 발생하지 않으면
        # 해저터널 생성
        cnt += 1
        # 하나의 묶음으로 만들어주기
        union(s, e)
        # 환경 부담금 ++
        hap_fee += w

        # 모든 섬이 연결되었다면 stop
        if cnt == N-1:
            break

    print(f'#{test_case} {round(hap_fee)}')