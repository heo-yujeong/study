# 부분집합의 합이 55 미만인 경우만 모은 부분집합(리스ㅡ)
N = 10
arr = list(range(1, 101))

for i in range(1, 1 << N): # 1024번의 경우의 수(공집합 제외)
    lst = []
    print(f'{i}번째 경우의 수')
    for j in range(N-1, -1, -1): # 해당 경우의 수에 arr의 j번째 요소 쓸거니?
        if i & (1 << j): # i번째 경우의 수에, j번째 요소가 포함되어 있는지를 확인
            lst.append(arr[j])
            if sum(lst) >= 20: # 부분집합의 합이 55 이상이 되면 조사 종료
                break
    if sum(lst) < 20:
        # return True
        print(lst) # 부분집합의 합이 55미만인 경우만 출력
