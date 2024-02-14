# K: 탐색 대상이 된 원소 번호
# result: 최종 결과 => 부분집합
# cnt: 부분집합의 합
def powerset(K, result, cnt):
    global count
    count += 1
    if cnt > 10:
        return
    if K == N: # 모든 원소에 대해 조사를 마쳤다면
        if cnt == 10: # 합이 10인 경우
            print(result)
        return
    else:
        # K번째 원소를 사용한 경우
        powerset(K+1, result+[arr[K]], cnt+arr[K])
        # K번째 원소를 사용하지 않은 경우
        powerset(K+1, result, cnt)


N = 10 # 원소의 개수
arr = list(range(1, 11))
count = 0
powerset(0, [], 0)
print(count)
# 백트래킹 하지 않았을 경우 2047번
# 했을 경우 415번