import sys
sys.stdin = open('input.txt')

for _ in range(10):
    test_case = int(input())
    # 2차원 배열의 양 옆에 0을 한 줄씩 더해주어 인덱스 error X
    mat = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    # 현재 위치(99행의 값이 2인 곳)
    current = [99, 0]
    for i in range(102):
        if mat[current[0]][i] == 2:
            current[1] = i

    d0 = [-1, 0, 0] # 위 왼 오
    d1 = [0, -1, 1] #  0  1  2
    idx = 0

    # 가장 위 행에 도착할 때까지 반복
    while current[0] > 0:
        # 왼쪽 이동(왼쪽에 1이 있을 때)
        if mat[current[0]][current[1]-1] == 1:
            idx = 1 # 방향 index = 1 => 왼쪽으로 이동
            # 왼쪽에 1이 있는 동안 반복
            while mat[current[0]][current[1]-1] == 1:
                # current[0] += d0[idx]
                current[1] += d1[idx]
            # 왼쪽에 0이 나오면 1칸 위로 이동(행의 값 -1)
            # 위의 조건이 없으면 위로는 올라가지 않고, 좌우로 왔다갔다만...
            current[0] -= 1

        # 오른쪽 이동(오른쪽에 1이 있을 때)
        elif mat[current[0]][current[1]+1] == 1:
            idx = 2 # 방향 index = 2 => 오른쪽으로 이동
            while mat[current[0]][current[1]+1] == 1:
                # current[0] += d0[idx]
                current[1] += d1[idx]
            current[0] -= 1

        # 왼쪽 & 오른쪽으로 갈 수 없음 => 위로 이동
        else:
            idx = 0 # 방향 index = 0 => 위로 이동
            current[0] += d0[idx]
            # current[1] += d1[idx]

    print(f'#{test_case} {current[1] - 1}')