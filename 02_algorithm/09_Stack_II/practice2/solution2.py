# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powerset중 원소의 합이 10인 부분집합
# 백트래킹을 추가하면?
# 마지막까지 부분집합을 결정하기 전에 합을 같이 계산해서
# 결정전에 합을 넘기면 가지치기


def f(i, k, s, t): # i-1 까지의 원소의 합 s를 함께 인자로 넘겨줌
    global cnt
    cnt += 1
    if s == t:
        for j in range(k):
            if bit[j]:
                print(A[j], end=' ')
        print()
    elif i == k: # 모든 원소를 고려했으나 s != t 인 경우
        return
    elif s > t: # i가 k가 되기 전에 이미 s가 t를 넘긴 경우
        return
    else:
        bit[i] = 1
        f(i+1, k, s+A[i], t)
        bit[i] = 0
        f(i+1, k, s, t)
        # 아래처럼 작성할 수도!
        # for j in range(1, -1, -1):
        #     bit[i] = j
        #     f(i+1, k, s+A[i]*j, t)



N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * N
cnt = 0
f(0, N, 0, 10)
print('cnt =', cnt) # 349
# soltion의 cnt횟수와 비교해보기!