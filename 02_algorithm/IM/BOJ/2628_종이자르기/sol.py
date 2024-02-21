import sys
sys.stdin = open('input.txt')

garo, sero = map(int, input().split())
board = [[0] * garo for _ in range(sero)]

N = int(input())
garo_cut = [0]
sero_cut = [0]

for _ in range(N):
    dir, num = map(int, input().split())
    if dir == 0:
        sero_cut.append(num)
    else:
        garo_cut.append(num)
garo_cut.append(garo)
sero_cut.append(sero)

garo_cut.sort()
sero_cut.sort()

for i in range(len(garo_cut)-1):
    garo_cut[i] = garo_cut[i+1]-garo_cut[i]
for i in range(len(sero_cut)-1):
    sero_cut[i] = sero_cut[i+1]-sero_cut[i]

garo_cut.pop()
sero_cut.pop()

space = []
for i in range(len(garo_cut)):
    for j in range(len(sero_cut)):
        space.append(garo_cut[i] * sero_cut[j])

print(max(space))