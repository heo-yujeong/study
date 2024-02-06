import sys
sys.stdin = open('input.txt')

# 슬라이싱으로 회문 판별하는 함수
def pal_1(word):
    result = 0
    reverse_word = word[::-1]

    if word == reverse_word:
        result = 1

    return result

# for 문으로 회문 판별하는 함수
def pal_2(word):
    result = 0
    cnt = 0
    for i in range(len(word)//2):
        if word[i] == word[-i-1]:
            cnt += 1
        if cnt == len(word)//2:
            result = 1

    return result

# while문으로 회문 판별하는 함수
def pal_3(word):
    result = 0
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            break
    else:
        result = 1

    return result

# 메서드와 빌트인 펑션으로 회문 판별하는 함수
def pal_4(word):
    result = 0

    if word == list(reversed(word)):
        result = 1

    return result


T = int(input())

for test_case in range(1, T+1):
    word = list(input())

    # result = pal_1(word)
    # result = pal_2(word)
    # result = pal_3(word)
    result = pal_4(word)

    print(f'#{test_case} {result}')