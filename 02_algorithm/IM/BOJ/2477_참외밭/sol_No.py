import sys
sys.stdin = open('input.txt')

N = int(input())

garo = []
sero = []

for _ in range(6):
    dir, length = map(int, input().split())
    if dir in [1, 2]:
        garo.append(length)
    else:
        sero.append(length)

area = max(garo)*max(sero) - min(garo)*min(sero)
print(area * N)