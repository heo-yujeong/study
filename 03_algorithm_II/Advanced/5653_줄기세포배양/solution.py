import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 비활성 dict => (좌표):[생명력, (0)시간++]
    #   time 지날때마다 시간 +1씩
    #   생명력 == 시간이 되면 제거 + 활성 dict에 add
    # 활성 dict => (좌표):[생명력, (0)시간++]
    #   1. time 지날때마다 시간 +1씩
    #   생명력 == 시간이 되면 제거 + dead_set에 add
    #   2. 활성 dict에 있는 것들 번식
    # 번식 dict => (좌표) : [값 들 중에 max]
    #   좌표 = 비활성, 활성, dead에 없는 값
    #   비활성 dict로 add할때는 (좌표):[생명력, 0]
    # dead_set = {(좌표), (좌표), ...}

    # 가로 => -K ~ M+K
    # 세로 => -K ~ N+K