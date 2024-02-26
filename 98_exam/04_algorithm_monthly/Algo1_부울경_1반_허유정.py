# import sys
# sys.stdin = open('algo1_sample_in.txt')

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # N: 돌의 개수, M: 뒤집기 횟수
    N, M = map(int, input().split())
    # 초기 상태(0: 흰색, 1: 검은색)
    # 작업 위치에서 인덱스를 바로 쓰기 위해 앞에 None 추가
    dol = [None] + list(map(int, input().split()))

    # M번 반복
    for n in range(M):
        # i: 기준 위치, j: 작업할 돌의 개수, w: 수행할 작업 번호
        i, j, w = map(int, input().split())

        # 작업번호가 1번이면
        # i번째부터 j개의 돌을 뒤집는다
        if w == 1:
            for a in range(i, i+j):
                # 돌이 있는 인덱스를 넘어가지 않을 때까지만 수행
                if a <= N:
                    dol[a] = 1 - dol[a]
        # 작업번호가 2번이면
        # i번째부터 j개의 돌을 i번째 돌의 색으로 바꾼다
        elif w == 2:
            for a in range(i, i+j):
                # 돌이 있는 인덱스를 넘어가지 않을 때까지만 수행
                if a <= N:
                    dol[a] = dol[i]
        # 작업번호가 3번이면
        # i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해
        # 같은 색이면 뒤집고, 다른 색이면 그대로 둔다
        else:
            idx = 1
            while True:
                # 뒤집기가 가능한 돌에 대해서만 수행
                # 인덱스를 넘어가면 멈춤
                if i-idx < 1 or i+idx >= N:
                    break
                # idx를 1개씩 증가시켜 j보다 커지면 종료
                if idx > j:
                    break
                # 돌의 색이 같으면 뒤집어 준다
                if dol[i-idx] == dol[i+idx]:
                    dol[i-idx] = 1 - dol[i-idx]
                    dol[i+idx] = 1 - dol[i+idx]
                # idx가 j가 될때까지 1씩 증가
                idx += 1

    print(f'#{test_case}', *dol[1:])