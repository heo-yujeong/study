import sys
sys.stdin = open('input.txt')

N = int(input())
len_list = [list(map(int, input().split())) for _ in range(6)]

garo_idx = sero_idx = 0
garo_max = sero_max = 0

for i in range(len(len_list)):
    if len_list[i][0] in [1, 2]:
        if garo_max < len_list[i][1]:
            garo_max = len_list[i][1]
            garo_idx = i
    else:
        if sero_max < len_list[i][1]:
            sero_max = len_list[i][1]
            sero_idx = i

garo_small = abs(len_list[(garo_idx - 1) % 6][1] - len_list[(garo_idx + 1) % 6][1])
sero_small = abs(len_list[(sero_idx - 1) % 6][1] - len_list[(sero_idx + 1) % 6][1])

area = garo_max*sero_max - garo_small*sero_small
print(area * N)