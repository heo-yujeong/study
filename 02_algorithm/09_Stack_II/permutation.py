# 1, 2, 3으로 만들 수 있는 순열

def f(i, k):
    if i == k:
        print(*P)
    else:
        for j in range(i, k): # P[i]와 자리를 바꿀 원소 P[j]
            P[i], P[j] = P[j], P[i] # 자리 교환
            f(i+1, k)
            P[i], P[j] = P[j], P[i] # 원상복구!

N = 3
P = [1, 2, 3]
f(0, N)