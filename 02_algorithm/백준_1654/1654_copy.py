import sys
sys.stdin = open('input.txt')

def lenth(array, min_len, max_len, target):
    if min_len > max_len:
        return max_len
    center = (min_len + max_len) // 2
    cnt = 0

    for arr in array:
        cnt += arr // center
    
    if cnt < target:
        return lenth(array, min_len, center-1, target)
    else:
        return lenth(array, center+1, max_len, target)


K, N = map(int, input().split())

bar = [int(input()) for _ in range(K)]

min_len = 1
max_len = max(bar)

result = lenth(bar, min_len, max_len, N)
print(result)




# while min_len <= max_len:
#     center_len = (min_len + max_len) // 2

#     sun_cnt = 0
#     for b in bar:
#         sun_cnt += b // center_len
    
#     if sun_cnt < N:
#         max_len = center_len -1
#     else:
#         min_len = center_len + 1


# print(max_len)