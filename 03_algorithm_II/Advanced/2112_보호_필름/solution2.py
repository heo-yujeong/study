import sys
sys.stdin = open('input.txt')
from itertools import combinations
from itertools import product

def per_test(film_arr):
    for j in range(W):
        fir_bar = film_arr[0][j]
        cell_cnt = 1
        for i in range(1, D):
            if film_arr[i][j] == fir_bar:
                cell_cnt += 1
                if cell_cnt >= K:
                    break
            else:
                fir_bar = film_arr[i][j]
                cell_cnt = 1
        if cell_cnt != K:
            return False
    return True

def comb():
    for cnt in range(1, D + 1):
        for choice in combinations(range(D), cnt):  # 약물 쓰는 행 개수에 대한 조합
            film_cp = [f[:] for f in film]
            for m in product([0, 1], repeat=cnt):  # 각 행에 어떤 약을 쓸지 조합
                for d in choice:
                    idx = choice.index(d)
                    film_cp[d] = medi[m[idx]]
                if per_test(film_cp):
                    return cnt

T = int(input())

for test_case in range(1, T+1):
    # 두께, 가로크기, 합격 기준
    D, W, K = map(int, input().split())
    # A: 0, B: 1
    film = [list(map(int, input().split())) for _ in range(D)]
    medi = [[0]*W, [1]*W]

    if K == 1 or per_test(film):
        input_cnt = 0
    else:
        input_cnt = comb()

    print(f'#{test_case} {input_cnt}')