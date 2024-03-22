import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline())
pq = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if pq:
            print(heappop(pq))
        else:
            print(0)
    else:
        heappush(pq, num)