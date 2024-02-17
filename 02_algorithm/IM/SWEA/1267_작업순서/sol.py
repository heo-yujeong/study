import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    working = [[] * (V+1) for _ in range(V+1)]
    # 작업 순서 표시할 리스트
    order = []

    for _ in range(E):
        # pre를 방문해야 next를 갈 수 있다
        pre, next = arr.pop(0), arr.pop(0)
        # next에서 pre로 간선 추가
        working[next].append(pre)

    while True:
        if len(order) == V:
            break

        # 시작점 = 먼저 해야할 작업이 없다
        # + 아직 수행하지 않은 일
        start_list = []
        for i in range(1, len(working)):
            if not working[i] and i not in order:
                start_list.append(i)
        # print('start', start_list)

        for start in start_list:
            # 시작점은 작업 내용에 추가하고
            order.append(start)
            # 다음 지점은 working에서 탐색
            for next in range(len(working)):
                # 다음번 위치에 시작점(이전 작업)이 있으면
                if start in working[next]:
                    # 작업이 끝났으니, 해당 내용은 다음번 위치에서 지움
                    working[next].remove(start)

    print(f'#{test_case}', *order)