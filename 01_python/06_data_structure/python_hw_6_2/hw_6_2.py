# 아래 함수를 수정하시오.
def remove_duplicates_to_set(num_list):
    return set(num_list)

# 가정 : arr에 1~9까지의 정수만 요소로 삽입된다면,
def remove_duplicates_to_set(arr):
    count_dict = {i: 0 for i in range(1, 10)} # dict_comprehension!
    for num in arr:
        count_dict[num] += 1 # {1: 1, 2: 2, 3: 1, 4: 2, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0}
    result = [key for key, item in count_dict.items() if item >= 1]

    return set(result)

def remove_duplicates_to_set(arr):
    count_list = [0 for i in range(10)]
    for index in arr:
        count_list[index] += 1 # [0, 1, 2, 1, 2, 1, 0, 0, 0, 0, 0]
    result = [num for num in range(len(count_list)) if count_list[num] >= 1]
    return set(result)

def remove_duplicates_to_set(arr):
    result = set()
    duplicate_check_dict = {}
    for num in arr:
        duplicate_check_dict[num] = duplicate_check_dict.get(num, 0) + 1
        if duplicate_check_dict[num] == 1:
            result.add(num)
    return result

result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
