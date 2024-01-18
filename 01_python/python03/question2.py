'''
numbers = []
my_dict = {'a' : 1}
numbers[0] = my_dict # 리스트의 특징 : 순서X!! 0번 인덱스라고 지정한 곳이 없음!
# 리스트 : 없는 인덱스에 직접 할다할 수 없다
#          => 리스트 + 리스트 or 리스트.append(요소) or 리스트.extend(요소 여러개) or 리스트.insert(위치, 값)

print(my_dict)
# IndexError: list assignment index out of range

'''

# 같은 기능의 다른 코드, 어떨때 어떻게 사용
# map, comprehension

# 각 문자열을 모두 정수로 바꿔서 리스트에 담으시오.
numbers_words = '1 2 3 4 5 6 7 8 9 10'

num_list = list(map(int, numbers_words.split()))
print(num_list)


num_list2 = []
for char in numbers_words.split():
    if char.isnumeric:
        num_list2.append(int(char))
print(num_list2)


# 각 문자열을 모두 정수로 바꿔서 2차원 리스트에 담으시오.
numbers_words2 = ['1 2 3 4 5', '6 7 8 9 10', '11 12 13 14 15']
num_list3 = []
for words in numbers_words2:
    conversion_list = list(map(int, words.split()))
    num_list3.append(conversion_list)

print(num_list3)

num_list4 = [list(map(int, words.split())) for words in numbers_words2]
print(num_list4)