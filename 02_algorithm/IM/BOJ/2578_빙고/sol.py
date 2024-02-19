import sys
sys.stdin = open('input.txt')

def isBingo():
    cnt = 0
    for i in range(5):
        if sum(board[i]) == 0:
            cnt += 1
    for j in range(5):
        hap = 0
        for i in range(5):
            hap += board[i][j]
        if hap == 0:
            cnt += 1
    diag = 0
    diag2 = 0
    for i in range(5):
        diag += board[i][i]
        diag2 += board[i][4-i]
    if diag == 0:
        cnt += 1
    if diag2 == 0:
        cnt += 1

    if cnt >= 3:
        return True
    else:
        return False

board = [list(map(int, input().split())) for _ in range(5)]

number = []
for _ in range(5):
    number.extend(map(int, input().split()))

for n in range(len(number)):
    for i in range(5):
        for j in range(5):
            if board[i][j] == number[n]:
                board[i][j] = 0
    check = isBingo()
    if check:
        print(n+1)
        break