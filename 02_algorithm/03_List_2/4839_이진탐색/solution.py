import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    # 책 페이지, A 목표 페이지, B 목표 페이지
    P, A, B = map(int, input().split())

    # A와 B의 왼쪽 = 1, 오른쪽 값 = 책페이지로 초기화
    a_left = 1
    b_left = 1
    a_right = P
    b_right = P
    # 목표 페이지 찾아가는 데 걸리는 횟수 초기화
    a_count = 0
    b_count = 0

    # A 탐색 횟수
    while True:
        # 중간 페이지 = int((왼쪽 + 오른쪽) / 2)
        a_center = int((a_left + a_right) / 2)
        if a_center == A: # 목표 페이지에 도달하면 반복 종료
            break
        elif a_center > A: # 중간페이지가 목표페이지보다 크다면
            a_right = a_center # 오른쪽 값을 목표 페이지로
            a_count += 1 # 카운트 1 증가
        else: # 중간페이지가 목표페이지보다 작다면
            a_left = a_center # 왼쪽 값을 목표 페이지로
            a_count += 1 # 카운트 1 증가

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