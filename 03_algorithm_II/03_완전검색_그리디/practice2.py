# 주사위 눈금 N개를 던져서 나올 수 있는 모든 조합

N = 3
path = []

def func(lev, start):
    if lev == N:
        print(path)
        return

    for i in range(start, 7):
        path.append(i)
        func(lev+1, i)
        path.pop()

func(0, 1)