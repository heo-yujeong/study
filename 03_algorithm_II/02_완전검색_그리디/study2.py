# 0 1 2 3 4 5 5 4 3 2 1 0 을 재귀호출 이용하여 구현
def KFC(x):
    if x == 6:
        return

    print(x, end=' ')
    KFC(x+1)
    print(x, end=' ')

KFC(0)