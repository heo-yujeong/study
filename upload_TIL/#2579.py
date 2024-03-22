n = int(input())
stair = [0] + [int(input()) for _ in range(n)]

if n < 2:
    print(sum(stair))
else:
    d = [0] * (n+1)
    d[1] = stair[1]
    d[2] = stair[1] + stair[2]
    for i in range(3, n+1):
        d[i] = max(d[i-2]+stair[i], d[i-3]+stair[i-1]+stair[i])

    print(d[n])