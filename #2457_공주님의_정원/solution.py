import sys
sys.stdin = open('input.txt')
from itertools import permutations

N = int(input())
monthly = {
    1 : [0]*31,
    2 : [0]*28,
    3 : [0]*31,
    4 : [0]*30,
    5 : [0]*31,
    6 : [0]*30,
    7 : [0]*31,
    8 : [0]*31,
    9 : [0]*30,
    10 : [0]*31,
    11 : [0]*30,
    12 : [0]*31
}

flowers = [list(map(int, input().split())) for _ in range(N)]
flo_chk = [0] * N

for i in range(1, N+1):
    permutations(flo_chk, i)

