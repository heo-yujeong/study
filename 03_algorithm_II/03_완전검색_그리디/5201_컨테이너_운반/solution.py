import sys
sys.stdin = open('input.txt')

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # N: 컨테이너 수, M: 트럭 수
    N, M = map(int, input().split())
    # N개의 화물의 무게
    wi = list(map(int, input().split()))
    # M개의 트럭의 적재 용량
    ti = list(map(int, input().split()))

    # 무게가 무거운 화물부터 정렬
    wi.sort(reverse=True)
    # 적재용량이 큰 트럭부터 정렬
    ti.sort(reverse=True)

    # 이동할 수 있는 화물의 무게를 담을 리스트
    move = []

    # (화물이 있는 동안) 트럭의 적재 용량이 화물의 무게보다 크면
    # 화물을 싣고, 화물 리스트에서 해당 화물 삭제
    for t in ti:
        if wi:
            for i in range(len(wi)):
                if t >= wi[i]:
                    move.append(wi[i])
                    wi.remove(wi[i])
                    break

    # 이동할 수 있는 화물 무게를 더함
    print(f'#{test_case} {sum(move)}')