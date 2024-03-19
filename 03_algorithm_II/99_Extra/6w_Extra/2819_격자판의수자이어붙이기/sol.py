import sys
sys.stdin = open('input.txt')

# 4방향 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 숫자 길이, 열, 행, 만들어지는 수
def backtrack(cnt, y, x, str_num):
    # 7자리 수가 만들어졌으면
    if cnt == 7:
        # 집합에 추가
        result.add(str_num)
        return

    # 4방향 탐색하면서
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 격자판 안에 있는 수라면
        if 0 <= nx < 4 and 0 <= ny < 4:
            # 해당 수를 뒤에 이어 붙이고 다음 자리로 탐색
            backtrack(cnt+1, ny, nx, str_num+str(board[ny][nx]))

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # 4 * 4 격자판
    board = [list(map(int, input().split())) for _ in range(4)]

    # 일곱자리 수를 저장할 집합
    # 중복허용하지 않기 위해 집합으로 초기화
    result = set()
    # 격자판을 모두 순회하면서 7자리 수 만들기
    for i in range(4):
        for j in range(4):
            backtrack(1, i, j, str(board[i][j]))

    print(f'#{test_case} {len(result)}')