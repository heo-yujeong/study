import sys
sys.stdin = open('input.txt')

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
    # 인자는 뭘받아야하지..
    # 일단 아래 cnt 받아서 몇개 줄?
    # 어디줄을 바꿀건지
    # 바꾸고 원상복구 하려면 배열 카피해서 해야하는거 아닌감
    # 00001...(1의 개수로 약품 사용횟수 나타낼수 있지않을까)
    # 1인 곳을 0으로 만들어보고 pertest =>  원상복구, 1로 만들어보고 pertest => 원상복구
    # 출력을 뭘로하지...
    # 약품 사용 횟수?
    # 점심식사때 계단 선택한거처럼... 모두 0번 or 모두 1번...
    pass

T = int(input())

for test_case in range(1, T+1):
    # 두께, 가로크기, 합격 기준
    D, W, K = map(int, input().split())
    # A: 0, B: 1
    film = [list(map(int, input().split())) for _ in range(D)]

    if K == 1 or per_test(film):
        input_cnt = 0
    else:
        for cnt in range(1, D+1):
            comb()

    print(f'#{test_case} {input_cnt}')