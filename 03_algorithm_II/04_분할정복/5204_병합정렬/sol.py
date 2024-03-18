import sys
sys.stdin = open('input.txt')
from collections import deque

# 분할
def merge_sort(lst):
    if len(lst) == 1:
        return lst

    left, right = [], []
    middle = len(lst) // 2

    for i in range(middle):
        left.append(lst[i])
    for i in range(middle, len(lst)):
        right.append(lst[i])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(deque(left), deque(right))

# 병합
def merge(left_lst, right_lst):
    global cnt
    # 정렬한 결과를 담을 리스트 초기화
    result = []

    # 왼쪽 마지막 요소가 오른쪽 마지막 원소보다 큰 경우
    if left_lst[-1] > right_lst[-1]:
        # cnt + 1
        cnt += 1

    # 왼쪽 리스트와 오른쪽 리스트가 모두 빌때까지 반복
    while left_lst or right_lst:
        # 두 리스트에 모두 값이 있는 경우
        if left_lst and right_lst:
            # 두 리스트 중 더 작은 요소를 result 리스트에 append
            if left_lst[0] <= right_lst[0]:
                result.append(left_lst.popleft())
            else:
                result.append(right_lst.popleft())
        # 왼쪽 리스트에만 값이 있는 경우
        elif left_lst:
            # 왼쪽 리스트의 앞의 값부터 result에 append
            result.append(left_lst.popleft())
        # 오른쪽 리스트에만 값이 있는 경우
        elif right_lst:
            # 오른쪽 리스트의 앞의 값부터 result에 append
            result.append(right_lst.popleft())

    # 정렬된 리스트 반환
    return result


# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # 정수의 개수
    N = int(input())
    # 정수들
    num_lst = list(map(int, input().split()))

    # 왼쪽 마지막 요소가 오른쪽 마지막 원소보다 큰 경우를 셀 변수
    cnt = 0
    # 병합 정렬
    sort_lst = merge_sort(num_lst)

    print(f'#{test_case} {sort_lst[N//2]} {cnt}')