import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    num_list = list(map(int, input()))
    counts = [0 for _ in range(10)]

    is_baby_gin = False
    cnt = 0
    idx = 0

    for num in num_list:
        counts[num] += 1

    while idx < len(counts):
        if counts[idx] >= 3:
            cnt += 1
            counts[idx] -= 3
            continue
        elif idx <= 7 and counts[idx] >= 1 and counts[idx+1] >= 1 and counts[idx+2] >= 1:
            cnt += 1
            counts[idx] -= 1
            counts[idx+1] -= 1
            counts[idx+2] -= 1
            continue
        idx += 1

    if cnt == 2:
        is_baby_gin = True
    print(f'#{test_case} {is_baby_gin}')