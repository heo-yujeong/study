import sys
sys.stdin = open('input.txt')

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # 돌아가야 할 학생 수
    N = int(input())
    # 복도를 따라 400개의 방 => 복도는 200개
    # 인덱스를 이용하기 위해 201개의 복도
    corridor = [0] * 201

    for _ in range(N):
        # 출발점, 도착점
        start, end = map(int, input().split())

        # 방번호 (1, 2), (3, 4)가 같은 복도를 이용하게 하기 위해
        # 방번호 + 1한 값을 2로 나눈 몫 == 복도 번호
        start = (start + 1) // 2
        end = (end + 1) // 2

        # 방번호가 작은 곳에서 큰 곳까지 복도에 + 1
        if start < end:
            for i in range(start, end+1):
                corridor[i] += 1
        else:
            for i in range(end, start+1):
                corridor[i] += 1

    # 복도에 적힌 수 = 해당 복도를 지나간 학생
    # 동시에 지나갈 수 없기 때문에 복도에 적힌 수 이상의 시간이 필요
    print(f'#{test_case} {max(corridor)}')