import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    pattern = input() # 찾을 패턴
    text = input() # 전체 텍스트

    # i: text의 인덱스, j: pattern의 인덱스
    i = j = 0
    while i < len(text) and j < len(pattern):
        if text[i] != pattern[j]:
            i -= j
            j = -1
        i += 1
        j += 1

    print(f'#{test_case}', end=' ')
    if j == len(pattern):
        print(1)
    else:
        print(0)