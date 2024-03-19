import sys
sys.stdin = open('input.txt')

def rotate(num, dir):
    check[num] = 1

    if num > 0:
        if mag[num][6] != mag[num-1][2] and not check[num-1]:
            rotate(num-1, dir*(-1))
    if num < 3:
        if mag[num][2] != mag[num+1][6] and not check[num+1]:
            rotate(num+1, dir*(-1))

    if dir == 1:
        mag[num] = [mag[num][-1]] + mag[num][:-1]
    else:
        mag[num] = mag[num][1:] + [mag[num][0]]

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