import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
temp = list(map(int, input().split()))

ondo = []

ondo.append(sum(temp[:K]))

for i in range(N-K):
    ondo.append(ondo[i] - temp[i] + temp[K+i])

print(max(ondo))