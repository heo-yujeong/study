import sys
sys.stdin = open('input.txt')

for _ in range(10):
    test_case = int(input())
    num_list = [list(map(int, input().split())) for _ in range(100)]

    sum_list = []

    # 각 행의 합
    for nums in num_list:
        sum_list.append(sum(nums))

    # 각 열의 합
    for i in range(100):
        col_sum = 0
        for j in range(100):
            col_sum += num_list[j][i]
        sum_list.append(col_sum)

    # 각 대각선의 합
    diag_sum_1 = 0 # 오른쪽으로 내려오는 대각선
    diag_sum_2 = 0 # 왼쪽으로 내려오는 대각선
    for i in range(100):
        diag_sum_1 += num_list[i][i] # 0 0, 1 1, 2 2, ... 99 99
        diag_sum_2 += num_list[i][99-i] # 0 99, 2 98, ... 99 0
    sum_list.append(diag_sum_1)
    sum_list.append(diag_sum_2)

    print(f'#{test_case} {max(sum_list)}')