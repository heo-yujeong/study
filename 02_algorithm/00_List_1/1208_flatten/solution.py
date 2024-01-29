import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    n = int(input())
    box_list = list(map(int, input().split()))
    for i in range(n):
        box_list[box_list.index(max(box_list))] -= 1
        box_list[box_list.index(min(box_list))] += 1
    print(f'#{test_case} {max(box_list)-min(box_list)}')