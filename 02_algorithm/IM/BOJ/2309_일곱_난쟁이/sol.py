import sys
sys.stdin = open('input.txt')

from itertools import combinations

height = [int(input()) for _ in range(9)]
comb = combinations(height, 7)

result = []
for com in comb:
    if sum(com) == 100:
        result.append(sorted(com))

for unit in result[0]:
    print(unit)