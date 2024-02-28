# 두명 이상의 친구들과 카페를 가는 경우의 수
arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

def get_count(tar):
    cnt = 0
    for i in range(n):
        if tar & 0x1:
            cnt += 1
        tar >>= 1
    return cnt

result = 0
for tar in range(1 << n):
    if get_count(tar) >= 2:
        result += 1

print(result)