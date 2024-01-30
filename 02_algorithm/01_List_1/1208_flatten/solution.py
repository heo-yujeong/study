import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    n = int(input())
    box_list = list(map(int, input().split()))
    for i in range(n): # 작업 횟수가 남아있는 동안
        box_list[box_list.index(max(box_list))] -= 1
        # 가장 많은 박스가 쌓인 인덱스를 찾아 해당 위치 박스 -1
        box_list[box_list.index(min(box_list))] += 1
        # 가장 적게 박스가 쌓인 인덱스를 찾아 해당 위치 박스 + 1
    print(f'#{test_case} {max(box_list)-min(box_list)}')