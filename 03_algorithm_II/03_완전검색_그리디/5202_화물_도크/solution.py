import sys
sys.stdin = open('input.txt')

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # 신청서 개수
    N = int(input())
    # [작업 시작시간, 종료시간] 리스트
    apply = [list(map(int, input().split())) for _ in range(N)]
    # 작업 종료시간이 빠른 순서 -> 작업 시작시간이 빠른 순서로 정렬
    apply.sort(key=lambda x: (x[1], x[0]))

    # 종료할 수 있는 작업을 count할 변수
    cnt = 0
    # 이전 작업이 끝난 시간
    # 처음에는 작업이 남아있지 않아 0으로 초기화
    pre_end = 0

    # 신청 리스트를 순회하면서
    for start, end in apply:
        # 이전 작업 완료시간이 시작 시간보다 작으면
        if pre_end <= start:
            # 이전 작업 완료 시간을 해당 작업의 완료시간으로 변경
            pre_end = end
            # count + 1
            cnt += 1

    print(f'#{test_case} {cnt}')