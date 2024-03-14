'''
블랙홀 & 웜홀 => {번호: [좌표, 좌표]} => -1이면 게임종료, 그 외이면 다른 좌표로 이동
핀볼 [좌표, 방향]
블록 방향 변경 => dict로 {블록번호: [ , , , ]} => 이전 방향 인덱스 자리에 바꿀 방향 번호 작성
벽 방향 변경 => 방향 반대로 & 이동 전 위치로 이동
블록 or 벽에 부딪힘 = 방향 변경 & 점수 +1
종료조건 : 처음 시작 위치에 도착하거나, 블랙홀을 만나거나
출발점 : 전체 순회하면서 (단, 웜홀, 블랙홀, 블럭이 아닌곳)
출발 방향 : 4방향 모두로 진행해볼것!
'''

# 상0 하1 좌2 우3
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

dir_trans = {1:[1, 3, 0, 2],
             2:[3, 0, 1, 2],
             3:[2, 0, 3, 1],
             4:[1, 2, 3, 0],
             5:[1, 0, 3, 2]}

import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    holes = {} # (i, j) = 행, 열
    # blocks = {}
    for i in range(N):
        for j in range(N):
            # if board[i][j] == -1:
            #     holes[-1] = (i, j)
            # elif board[i][j] in range(1, 6):
            #     if blocks.get(board[i][j], None) == None:
            #         blocks[board[i][j]] = [(i, j)]
            #     else:
            #         blocks[board[i][j]].append((i, j))
            if board[i][j] in range(6, 11):
                if holes.get(board[i][j], None) == None:
                    holes[board[i][j]] = [(i, j)]
                else:
                    holes[board[i][j]].append((i, j))

    print(holes)
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for dir in range(4):
                    pass
                    # 함수 구현하자....