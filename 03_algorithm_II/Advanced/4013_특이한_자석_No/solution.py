import sys
sys.stdin = open('input.txt')

def rotate(num, dir):
    check[num] = 1
    # 자성 다를 경우 회전!!!!
    # 본인 기준 오른쪽 자석과 왼쪽 자석 모두 생각해야함!
    # 회전 후에 리스트 순서 맞추기!



T = int(input())

for test_case in range(1, T+1):
    K = int(input())
    mag = [list(map(int, input().split())) for _ in range(4)]

    for _ in range(K):
        num, dir = map(int, input().split())
        check = [0] * 4
        rotate(num-1, dir)

    jumsu = 0
    for i in range(4):
        jumsu += mag[i][0] * 2 ** i

    print(f'#{test_case} {jumsu}')