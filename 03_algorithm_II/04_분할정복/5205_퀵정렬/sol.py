import sys
sys.stdin = open('input.txt')

# 퀵 정렬
def quick_sort(lst, start_idx, last_idx):
    if start_idx < last_idx:
        # 분할 과정을 통해 피벗을 구한 후
        pivot_idx = partition(lst, start_idx, last_idx)
        # 피벗보다 작은 값들에 대해 퀵 정렬 수행
        quick_sort(lst, start_idx, pivot_idx-1)
        # 피벗보다 큰 값들에 대해 퀵 정렬 수행
        quick_sort(lst, pivot_idx+1, last_idx)

# 분할
def partition(lst, start_idx, last_idx):
    # 피봇 = 가장 앞의 인덱스 값으로
    pivot = lst[start_idx]
    # i는 왼쪽부터 오른쪽으로 탐색, j는 오른쪽에서 왼쪽으로 탐색
    i, j = start_idx, last_idx
    # i와 j가 교차될 때까지 반복
    while i <= j:
        # 피봇보다 큰 값이 나올때까지 i + 1
        while i <= j and lst[i] <= pivot:
            i += 1
        # 피봇보다 작은 값이 나올때까지 j - 1
        while i <= j and lst[j] >= pivot:
            j -= 1
        # 결정된 i, j에 대해 j가 i보다 크면
        if i < j:
            # 두개의 요소 교환
            lst[i], lst[j] = lst[j], lst[i]

    # i, j가 교차되어서 while 반복문을 벗어나면
    # 피벗 값을 가운데 배치
    # => 피벗보다 작은 값 / 피벗 / 피벗보다 큰 값
    lst[start_idx], lst[j] = lst[j], lst[start_idx]
    return j

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # 정수의 개수
    N = int(input())
    # 정수들
    num_lst = list(map(int, input().split()))

    # 퀵 정렬
    quick_sort(num_lst, 0, N-1)

    print(f'#{test_case} {num_lst[N//2]}')