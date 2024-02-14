import sys
sys.stdin = open('input.txt')

def f(i, k):
    global min_v
    global cnt
    cnt += 1
    if i == k:
        s = 0 # 선택한 원소의 합
        for j in range(k):
            s += arr[j][P[j]] # j행에서 P[j]열을 고른 경우 합에 더함
        if min_v > s:
            min_v = s
    else:
        for j in range(i, k):
            P[i], P[j] = P[j], P[i]
            f(i+1, k)
            P[i], P[j] = P[j], P[i]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    min_v = 100
    cnt = 0
    f(0, N)
    print(min_v)
    print('cnt =', cnt) # 16 16 326