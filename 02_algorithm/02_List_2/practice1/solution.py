import sys
from pprint import pprint
sys.stdin = open('input.txt')

arr = [list(map(int, input().split())) for _ in range(5)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

result = [[0] * 5 for _ in range(5)]

for i in range(5):
    for j in range(5):
        hap_abs = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 5 and 0 <= nj < 5:
                hap_abs += abs(arr[ni][nj] - arr[i][j])
        result[i][j] = hap_abs

pprint(result)