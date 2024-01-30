import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split()) # 퍼즐크기 N*N, 단어길이 K
    puzzle = [input() for _ in range(N)]

    result = 0
    # 가로
    for i in range(len(puzzle)):
        for puz in puzzle[i].split('0'): # 0을 기준으로 나눔
            if len(puz.replace(' ','')) == K:
            # 문자는 공백도 길이이기 때문에 제거
                result += 1

    # 세로 => 전치행렬을 만들어 위와 같은 작업 반복
    for i in range(len(puzzle)):
        puzzle[i] = list(puzzle[i].split())
    puzzle_t = (list(map(list, zip(*puzzle)))) # 전치행렬
    for i in range(len(puzzle_t)):
        temp = ''
        for j in range(len(puzzle_t)):
             temp += str(puzzle_t[i][j])
        puzzle_t[i] = temp # 리스트를 문자열로 변환

    for i in range(len(puzzle_t)):
        for puz in puzzle_t[i].split('0'):
            if len(puz) == K:
                result += 1

    print(f'#{test_case} {result}')