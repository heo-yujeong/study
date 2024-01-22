# 아래 함수를 수정하시오.
def capitalize_words(args):
    cap_word = args.title()
    return cap_word

# 반복문으로
def capitalize_words(word):
    result = ''
    temp = ''
    for index, char in enumerate(word):
        if index == 0 or temp == ' ':
            result += char.upper()
        else:
            result += char
        temp = char
    return result

# enumerate와 range로 순회하는 차이
# range로 범위를 산정한 경우 index만 나오기 때문에 요소를 보려면 word[index]형식으로 작성해야 함
# enumerate는 index는 index대로, 요소 자체는 요소대로 사용 가능

result = capitalize_words("hello, world!")
print(result)