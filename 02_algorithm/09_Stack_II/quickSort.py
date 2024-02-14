def quick_sort(start, end):
    stack = [(start, end)]
    while stack:
        start, end = stack.pop()
        if start < end:
            pivot_index = partition(start, end)
            stack.append((start, pivot_index-1))
            stack.append((pivot_index+1, end))

def partition(start, end):
    pivot = arr[end]
    i = start - 1 # pivot이 들어갈 위치
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i + 1


arr = [3, 6, 8, 10, 1, 2, 1]
N = len(arr)
quick_sort(0, N-1)
print(arr)