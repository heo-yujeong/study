import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    num_list = input().split('0')
    # '0'으로 구분하면, 111, 11, 이런식의 리스트 생성

    count = []
    for num in num_list:
        count.append(len(num)) # 리스트를 순회하며 각 길이 구함

    print(f'#{test_case} {max(count)}')