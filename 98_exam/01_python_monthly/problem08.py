############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count()를 사용하지 않습니다.
def find_solo(number_list):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    result = 0 # 짝이 맞지 않는 정수를 담을 변수
    number_count_dict = {} # 리스트에 정수가 몇개씩 들어있는지 count할 dict
    for number in number_list: # 리스트를 모두 순회하는 동안
        number_count_dict[number] = number_count_dict.get(number, 0) + 1 # 해당 정수를 키로 하는 value + 1
    for key, value in number_count_dict.items(): # dict의 key 와 value를 순회하면서
        if value == 1: # value가 1이면 (=> 리스트에서 한 번만 조회 되었다면)
            result = key # 그때의 key값이 짝이 맞지 않은 정수!

    return result


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
number_list1 = [64, 27, 71, 27, 64]
print(find_solo(number_list1))  # 71
number_list2 = [4, 14, 60, 14, 49, 49, 78, 60, 78]
print(find_solo(number_list2))  # 4
#####################################################
