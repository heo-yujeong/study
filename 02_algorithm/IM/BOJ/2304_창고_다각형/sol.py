import sys
sys.stdin = open('input.txt')

N = int(input())
max_height = 0
max_loc = 0
dot_height = []
for _ in range(N):
    l, h = map(int, input().split())
    dot_height.append([l, h])
    if max_height < h:
        max_height = h
        max_idx = l
    if max_loc < l:
        max_loc = l

pillar = [0] * (max_loc + 1)
for l, h in dot_height:
    pillar[l] = h

result = 0
left_height = 0
right_height = 0

for i in range(max_idx+1):
    if left_height < pillar[i]:
        left_height = pillar[i]
    result += left_height
for i in range(max_loc, max_idx, -1):
    if right_height < pillar[i]:
        right_height = pillar[i]
    result += right_height

print(result)