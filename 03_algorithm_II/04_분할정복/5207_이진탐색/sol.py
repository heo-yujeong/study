import sys
sys.stdin = open('input.txt')

# 이진 탐색 수행
def binary_search(dir, start, end, target):
    # 시작인덱스가 마지막 인덱스보다 커지면
    # target이 리스트안에 없다는 뜻
    if start > end:
        # -1를 return하고 종료
        return -1

    # 중앙인덱스 = (시작인덱스 + 마지막인덱스) // 2
    mid = (start + end) // 2
    # target과 중앙 인덱스의 값이 같으면
    # 리스트안에 target이 존재하면
    if target == A[mid]:
        # 중앙 인덱스 반환
        # -1을 반환하지만 않으면 count + 1이 됨!
        return mid

    # target이 리스트의 중앙값보다 작으면
    # 중앙값보다 작은 값들을 탐색해야함
    if target < A[mid]:
        # 이전에 방향이 왼쪽이면 동일한 방향을 탐색하는 것이기 때문에
        if dir == 'l':
            # -1을 return 하고 종료
            return -1
        # 방향이 다르면 방향값을 왼쪽으로 바꾸고
        # 마지막 인덱스를 중앙값보다 1 작은 값으로 바꿔서 재귀
        return binary_search('l', start, mid-1, target)
    # target이 리스트의 중앙값보다 크면
    # 중앙값보다 큰 값을 탐색해야함
    else:
        # 이전에 방향이 오른쪽이면 동일한 방향을 탐색하는 것이기 때문에
        if dir == 'r':
            # -1을 return 하고 종료
            return -1
        # 방향이 다르면 방향값을 오른쪽으로 바꾸고
        # 시작 인덱스를 중앙값보다 1 큰 값으로 바꿔서 재귀
        return binary_search('r', mid+1, end, target)

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # N: A 리스트의 요소 개수. M: B 리스트의 요소 개수
    N, M = map(int, input().split())
    # A 리스트의 값
    A = list(map(int, input().split()))
    # 이진탐색은 정렬된 값에 대해 사용 가능!
    A.sort()
    # A에 속해 있으면서, 탐색 과정에서 양쪽 구간을
    # 번갈아 선택하게 되는 숫자의 개수를 count할 변수
    cnt = 0

    # B리스트를 순회하면서
    for num in map(int, input().split()):
        # 이진 탐색을 수행해서 결과가 -1이 아니면
        # => 문제에서 요구하는 대로 이진 탐색을 수행했다면
        if binary_search(0, 0, N-1, num) != -1:
            # count + 1
            cnt += 1

    print(f'#{test_case} {cnt}')