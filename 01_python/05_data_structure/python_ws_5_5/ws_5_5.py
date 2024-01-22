# 아래 함수를 수정하시오.
def even_elements(args):
    pop_list = []
    for arg in args:
        if arg % 2 == 0:
            pop_list.extend([args.pop(args.index(arg))])
    return pop_list        
            

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
