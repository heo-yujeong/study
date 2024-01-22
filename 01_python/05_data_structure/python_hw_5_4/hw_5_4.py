# 아래 함수를 수정하시오.
def find_min_max(args):
    min_val = min(args)
    max_val = max(args)
    return min_val, max_val
# 파이썬 함수는 반드시 반환하는 값이 하나의 객체
# 2개 이상의 객체를 반환하려면 파이썬이 알아서 tuple로 묶어서 반환

def find_max(arr):
    result = 0
    for num in arr:
        if result < arr:
            result = num
    return result 

def find_min(arr):
    result = arr[0]
    for num in arr:
        if result > num:
            result = num
    return result

def find_min_max(arr):
    max_result = 0
    min_result = arr[0]

    for num in arr:
        if max_result < num:
            max_result = num
        if min_result > num:
            min_result = num
    return min_result, max_result



result = find_min_max([3, 1, 7, 2, 5]) #6
print(result)  # (1, 7)