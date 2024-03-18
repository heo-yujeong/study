arr = [324, 32, 22114, 16, 48, 93, 422, 21, 316]

# 정렬된 상태의 데이터
arr.sort()

# 이진검색 - 반복문
def binarySearch(target):
    low = 0
    high = len(arr) - 1
    cnt = 0

    while low <= high:
        mid = (low + high) // 2
        # print(f'mid={mid} / arr[mid]={arr[mid]}')
        cnt += 1
        if arr[mid] == target:
            return mid, cnt
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1, cnt

print(f'21 = {binarySearch(21)}')
print(f'324 = {binarySearch(324)}')
print(f'888 = {binarySearch(888)}')


# 이진검색 - 재귀함수
def binarySearch_recur(low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2
    if target == arr[mid]:
        return mid

    if target < arr[mid]:
        return binarySearch_recur(low, mid-1, target)
    else:
        return binarySearch_recur(mid+1, high, target)

print(f'21 = {binarySearch_recur(0, len(arr)-1, 21)}')
print(f'324 = {binarySearch_recur(0, len(arr)-1, 324)}')
print(f'888 = {binarySearch_recur(0, len(arr)-1, 888)}')