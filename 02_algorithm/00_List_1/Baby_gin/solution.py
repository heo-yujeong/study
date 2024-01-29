import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    num_list = list(map(int, input()))
    counts = [0 for _ in range(10)]

    is_baby_gin = False
    cnt_triplet = 0
    cnt_run = 0

    for num in num_list:
        counts[num] += 1

    for i in range(10):
        if counts[i] >= 3:
            cnt_triplet += 1
            counts[i] -= 3
    for i in range(8):
        if counts[i] == counts[i+1] == counts[i+2] == 1:
            cnt_run += 1
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
    if cnt_triplet == 2 or cnt_triplet == 2 or (cnt_triplet == 1 and cnt_run == 1):
        is_baby_gin = True
    print(f'#{test_case} {is_baby_gin}')