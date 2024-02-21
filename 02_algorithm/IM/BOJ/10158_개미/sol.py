import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

dx = dy = 1

for _ in range(t, 0, -1):
    nx = p + dx
    ny = q + dy
    if 0 <= nx <= w and 0 <= ny <= h:
        p, q = nx, ny
        if p == 0 or p == w:
            dx = -dx
        if q == 0 or q == h:
            dy = -dy
print(p, q)