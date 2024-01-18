food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.
print('-' * 20, 'for문', '-' * 20)
for i in range(len(food_list)):
    if food_list[i]['이름'] == '토마토':
        food_list[i]['종류'] = '과일'
    if food_list[i]['이름'] == '자장면':
        print('자장면엔 고춧가루지')
    print(food_list[i]['이름'], '은/는', food_list[i]['종류'], '(이)다.')

print(food_list)

print()
print('-' * 20, 'while문', '-' * 20)
list_index = 0
while True:
    if food_list[list_index]['이름'] == '토마토':
        food_list[list_index]['종류'] = '과일'
    if food_list[list_index]['이름'] == '자장면':
        print('자장면엔 고춧가루지')
    print(food_list[list_index]['이름'], '은/는', food_list[list_index]['종류'], '(이)다.')
    list_index += 1
    if list_index == len(food_list):
        break

print(food_list)