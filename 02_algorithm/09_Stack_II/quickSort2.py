def quick_sort(lst):
    if len(lst) <= 1:
        return lst
        # 정렬대상을 분할하다가 더 이상 분할할 수 없을 때 반환
    else:
        pivot = lst[0]
        # pivot 보다 작은 대상, 큰 대상 모음
        less_than_pivot = [x for x in lst[1:] if x <= pivot]
        greater_than_pivot = [x for x in lst[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

arr = [3, 6, 8, 10, 1, 2, 1]
N = len(arr)
result = quick_sort(arr)
print(result)