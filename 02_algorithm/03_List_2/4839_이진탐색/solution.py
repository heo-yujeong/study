import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    P, A, B = map(int, input().split())

    a_left = 0
    b_left = 0
    a_right = P
    b_right = P
    a_count = 0
    b_count = 0

    # A 탐색 횟수
    while True:
        a_center = int((a_left + a_right) / 2)
        if a_center == A:
            break
        elif a_center > A:
            a_right = a_center
            a_count += 1
        else:
            a_left = a_center
            a_count += 1

    # B 탐색 횟수
    while True:
        b_center = int((b_left + b_right) / 2)
        if b_center == B:
            break
        elif b_center > B:
            b_right = b_center
            b_count += 1
        else:
            b_left = b_center
            b_count += 1

    if a_count > b_count:
        print(f'#{test_case} B')
    elif a_count < b_count:
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} 0')