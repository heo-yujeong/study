import sys
from heapq import heappush, heappop

T = int(sys.stdin.readline())
for _ in range(T):
    pq = []
    k = int(sys.stdin.readline())
    for _ in range(k):
        oper, num = sys.stdin.readline().split()
        print(oper, num)
        if oper == 'I':
            heappush(pq, int(num))
        else:
            if pq:
                if num == 1:
                    heappop(pq)
                else:
                    heappop(pq)
        print(pq)
    if pq:
        print('최대, 최소')
    else:
        print('EMPTY')