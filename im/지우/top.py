import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, M, m = map(int, input().split())
    block = list(map(int, input().split()))
    block.sort()

    if M < m:
        M, m = m, M

    result = 0
    while M != m:
        cur = block.pop(0)
        result += M*cur
        M -= 1

    while M != 0:
        l, r = block.pop(0), block.pop(0)
        result += M * (l + r)
        M -= 1

    print(f'#{tc} {result}')
