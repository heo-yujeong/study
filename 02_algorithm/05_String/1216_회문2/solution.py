import sys
sys.stdin = open('input.txt')

def search_pal(arr):
    for k in range(100, 1, -1):
        for i in range(100):
            for j in range(100-k+1):
                if arr[i][j:j+k] == arr[i][j:j+k][::-1]:
                    return k

for _ in range(10):
    test_case = int(input())
    board = [input() for _ in range(100)]

    # 가로 탐색
    k1 = search_pal(board)

    board_t = [''.join(list(i)) for i in zip(*board)]
    # 세로 탐색
    k2 = search_pal(board_t)

    print(f'#{test_case} {max(k1, k2)}')