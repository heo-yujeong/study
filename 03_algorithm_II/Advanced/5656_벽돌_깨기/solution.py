import sys
sys.stdin = open('input.txt')
from collections import deque

dw = [0, 0, -1, 1]
dh = [-1, 1, 0, 0]

def cnt_remove(h, w, arr):
    queue = deque()
    queue.append([h, w, arr[h][w]])
    arr[h][w] = 0
    cnt = 1

    while queue:
        h, w, rem_len = queue.popleft()

        for idx in range(4):
            for l in range(1, rem_len):
                nw = w + dw[idx]*l
                nh = h + dh[idx]*l
                if 0 <= nw < W and 0 <= nh < H and arr[nh][nw]:
                    queue.append([nh, nw, arr[nh][nw]])
                    arr[nh][nw] = 0
                    cnt += 1
    return cnt

def move_brick(arr):
    for w in range(W):
        idx = H-1
        for h in range(H-1, -1, -1):
            if arr[h][w]:
                if idx != h:
                    arr[idx][w], arr[h][w] = arr[h][w], arr[idx][w]
                idx -= 1

def remove_brick(round, cnt, brick):
    global max_cnt
    if round == N:
        if max_cnt < cnt:
            max_cnt = cnt
        return

    for w in range(W):
        brick_cp = [b[:] for b in brick]
        h = 0
        while h < H and not brick_cp[h][w]:
            h += 1

        remove_cnt = 0
        if h < H:
            remove_cnt = cnt_remove(h, w, brick_cp)
            move_brick(brick_cp)
        remove_brick(round+1, cnt+remove_cnt, brick_cp)


T = int(input())

for test_case in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    total_brick = 0
    for h in range(H):
        for w in range(W):
            if bricks[h][w] != 0:
                total_brick += 1
    max_cnt = 0
    remove_brick(0, 0, bricks)

    print(f'#{test_case} {total_brick-max_cnt}')