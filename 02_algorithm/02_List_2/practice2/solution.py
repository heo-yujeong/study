# 부분집합 합 문제 구현하기
# 10개의 정수를 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지를 계산하는 함수
# -7 -5 2 3 8 -2 4 6 9
import sys
sys.stdin = open('input.txt')

def f(arr, N):
    for i in range(1, 1 << N): # 1024번의 경우의 수(공집합 제외)
        print(f'{i}번째 경우의 수')
        lst = []
        for j in range(N): # 해당 경우의 수에 arr의 j번째 요소 쓸거니?
            if i & (1 << j): # i번째 경우의 수에, j번째 요소가 포함되어 있는지를 확인
                lst.append(arr[j])
        print(lst)
        print(sum(lst))
        if sum(lst) == 0:
            # return True
            pass
    return False

N = int(input())
arr = list(map(int, input().split()))
print(f(arr, N))