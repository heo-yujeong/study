import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    is_sdoku = 0
    cnt = 0 # 27이 되면 겹치지 않음!

    # 가로
    for puz in puzzle:
        if sorted(puz) == list(range(1, 10)):
            cnt += 1

    # 세로
    puzzle_t = list(map(list, zip(*puzzle)))
    for puz in puzzle_t:
        if sorted(puz) == list(range(1, 10)):
            cnt += 1

    # 3 * 3
    for k in [0, 3, 6]:
        for l in [0, 3, 6]:
            temp = []
            for i in range(3):
                for j in range(3):
                    temp.append(puzzle[k+i][l+j])
            if sorted(temp) == list(range(1, 10)):
                cnt += 1

    if cnt == 27:
        is_sdoku = 1

    print(f'#{test_case} {is_sdoku}')