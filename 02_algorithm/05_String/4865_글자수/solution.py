import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    str1 = input() # 키 값
    str2 = input()

    distinct_str1 = []
    for char in str1:
        if char not in distinct_str1:
            distinct_str1.append(char)

    counts = [0] * len(distinct_str1)

    for char in str2:
        if char in distinct_str1:
            counts[distinct_str1.index(char)] += 1

    print(f'#{test_case} {max(counts)}')