# 아래 함수를 수정하시오.
def reverse_string(char):
    return ''.join(list(reversed(char)))

# 반복문으로
def reverse_string(word):
    result = ''
    for index in range((len(word))-1, -1, -1):
        result += word[index]
    return result

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH