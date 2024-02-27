import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    board, num = input().split()
    board = list(map(int, board))
    num = int(num)




    print(f'#{test_case} {board}')