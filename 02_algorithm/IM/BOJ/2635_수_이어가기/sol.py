import sys
sys.stdin = open('input.txt')

N = int(input())

result = []

for i in range(1, N+1):
    tmp = [N]
    tmp.append(i)

    idx = 1
    while True:
        next = tmp[idx-1] - tmp[idx]
        if next < 0:
            break
        else:
            tmp.append(next)
            idx += 1
    if len(result) < len(tmp):
        result = tmp

print(len(result))
print(*result)