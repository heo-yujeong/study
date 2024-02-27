import sys
sys.stdin = open('input.txt')

def search(now, acc):
    global result
    if acc > result:
        return
    if all(visited):
        acc += area[now][0]
        if result > acc:
            result = acc
    else:
        for next in range(1, N):
            if now != next and not visited[next]:
                visited[next] = 1
                search(next, acc+area[now][next])
                visited[next] = 0

    return result

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]

    result = 101 * N
    visited = [0] * N
    visited[0] = 1

    search(0, 0)

    print(f'#{test_case} {result}')