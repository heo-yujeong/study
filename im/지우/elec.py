import sys
sys.stdin = open('a2.txt')


for tc in range(1, int(input())+1):
    N = int(input())
    home = []

    for _ in range(N):
        x, y, d = map(int, input().split())
        x += 15
        y += 15
        home.append((x, y, d))

    arr = [[0] * 31 for _ in range(31)]
    mx = 0
    for h in home:
        x, y, d = h
        for i in range(-d, d+1):
            for j in range(-d, d+1):
                if abs(i) + abs(j) <= d:
                    nx, ny = x + i, y + j
                    if 0 <= nx < 31 and 0 <= ny < 31:
                        arr[nx][ny] += 1
                        mx = max(arr[nx][ny], mx)

    result = 31*20
    if mx == N:
        for i in range(31):
            for j in range(31):
                if arr[i][j] == mx:
                    tmp = 0
                    for h in home:
                        x, y, d = h
                        tmp += abs(x-i) + abs(y-j)
                    result = min(result, tmp)
    elif N == 2:
        result = 2

    elif N > mx+2:
        result = -1

    else:
        e = mx
        s = N - e
        while s <= e:
            if s == e:
                for i in range(31):
                    for j in range(31):
                        if arr[i][j] == mx:
                            tmp = 0
                            for h in home:
                                x, y, d = h
                                tmp += abs(x - i) + abs(y - j)
                            result = min(result, tmp)
            else:
                visit_h = [0 for _ in range(N)]
                tmp = 0
                for i in range(31):
                    for j in range(31):
                        if arr[i][j] == e:
                            for n, h in enumerate(home):
                                x, y, d = h
                                tmp += abs(x-i) + abs(y-j)
                                visit_h[n] = 1

                for i in range(31):
                    for j in range(31):
                        if arr[i][j] == s:
                            for n, h in enumerate(home):
                                if not visit_h[n]:
                                    x, y, d = h
                                    tmp += abs(x-i) + abs(y-j)
                        for i in visit_h:
                            if not i:
                                break
                        else:
                            result = min(result, tmp)
            s += 1
            e -= 1
    print(f'#{tc} {result}')
