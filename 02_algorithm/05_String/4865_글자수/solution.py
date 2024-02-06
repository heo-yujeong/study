import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    str1 = input() # 키 값
    str2 = input()

    # 키 값이 되는 리스트의 중복값 제거
    distinct_str1 = []
    for char in str1:
        if char not in distinct_str1:
            distinct_str1.append(char)

    # 중복 제거된 키 만큼 카운트 배열 생성
    counts = [0] * len(distinct_str1)

    # 각 값이 몇번 나왔는지 체크
    # 단, 값이 키 배열에 있는 경우에만
    for char in str2:
        if char in distinct_str1:
            counts[distinct_str1.index(char)] += 1

    print(f'#{test_case} {max(counts)}')