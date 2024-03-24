N, r, c = map(int, input().split())

result = 0
while N > 0:
    if r < 2**(N-1) and c < 2**(N-1):
        result += (2 ** N) * 0 * (2 ** (N-2))
    elif r < 2**(N-1) and c >= 2**(N-1):
        result += (2 ** N) * 1 * (2 ** (N-2))
        c -= 2**(N-1)
    elif r >= 2**(N-1) and c < 2**(N-1):
        result += (2 ** N) * 2 * (2 ** (N-2))
        r -= 2**(N-1)
    else:
        result += (2 ** N) * 3 * (2 ** (N-2))
        r -= 2 ** (N-1)
        c -= 2 ** (N-1)
    N -= 1

print(int(result))