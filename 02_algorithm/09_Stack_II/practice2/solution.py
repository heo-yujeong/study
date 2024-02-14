# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powerset중 원소의 합이 10인 부분집합

# f(i, k) => bit[i]를 결정하는 함수
def f(i, k, t): # 부분집합의 합이 t인 경우 찾기!
    global cnt
    cnt += 1
    if i == k: # 모든 원소에 대해 결정했다면
        sum_sub = 0
        for j in range(k):
            if bit[j]: # A[j]가 부분집합에 포함된 경우
                sum_sub += A[j]
                # print(A[j], end=' ')
        # print(f'=> 합: {sum_sub}')
        if sum_sub == t:
            for j in range(k):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    else:
        bit[i] = 1
        f(i+1, k, t)
        bit[i] = 0
        f(i+1, k, t)
        # 아래처럼 작성할 수도!
        # for j in range(1, -1, -1):
        #     bit[i] = j
        #     f(i+1, k, t)


N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * N # bit[i] => A[i]가 부분집합에 포함되는지 표시
cnt = 0
f(0, N, 10)
print('cnt =', cnt) # 2047번