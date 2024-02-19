import sys
sys.stdin = open('input.txt')

garo, sero = map(int, input().split())
store_cnt = int(input())
store = []
for _ in range(store_cnt):
    dir, step = map(int, input().split())
    store.append([dir, step])
dir, step = map(int, input().split())

cnt = 0
for d, s in store:
    if dir == 1:
        if d == 1:
            cnt += abs(step - s)
        elif d == 2:
            cnt += min(step + sero + s, garo-step + sero + garo-s)
        elif d == 3:
            cnt += (step + s)
        else:
            cnt += (garo-step + s)
    elif dir == 2:
        if d == 1:
            cnt += min(step + sero + s, garo-step + sero + garo-s)
        elif d == 2:
            cnt += abs(step - s)
        elif d == 3:
            cnt += (step + sero-s)
        else:
            cnt += (garo-step + sero-s)
    elif dir == 3:
        if d == 1:
            cnt += (step + s)
        elif d == 2:
            cnt += (sero-step + s)
        elif d == 3:
            cnt += abs(step - s)
        else:
            cnt += min(step + garo + s, sero-step + garo + sero-s)
    else:
        if d == 1:
            cnt += (step + garo-s)
        elif d == 2:
            cnt += (garo-s + sero-step)
        elif d == 3:
            cnt += min(step + garo + s, sero-step + garo + sero-s)
        else:
            cnt += abs(step - s)

print(cnt)