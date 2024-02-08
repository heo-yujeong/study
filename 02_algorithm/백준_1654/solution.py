import sys
sys.stdin = open('input.txt')


K, N = map(int, input().split())
line = [int(input()) for i in range(K)]

# 이진 탐색
def length(line, start, end):
    global N
    if abs(start - end) == 1:
        return end

    mid = (start + end) // 2

    cnt = 0 # mid 길이로 잘랐을 때 나오는 줄의 갯수
    for l in line:
        cnt += (l // mid)

    if cnt >= N:  # 갯수보다 많으면 자르는 크기를 늘려도 된다
        return length(line, mid, end)

    elif cnt < N:   # 갯수보다 적으면 자르는 크기 줄여야 된다.
        return length(line, start, mid)


result = length(line, 1, max(line))
# print(max(mid_lst))
print(result)