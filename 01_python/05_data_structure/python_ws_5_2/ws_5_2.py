# 아래 함수를 수정하시오.
def remove_duplicates(args):
    new_lst = []
    lst_to_set = set(args)
    for lts in lst_to_set:
        new_lst.append(lts)
    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
