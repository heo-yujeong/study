# 아래 함수를 수정하시오.
def sort_tuple(args):
    new_tuple = ()
    args = list(args)
    args.sort()
    new_tuple = tuple(args)
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
