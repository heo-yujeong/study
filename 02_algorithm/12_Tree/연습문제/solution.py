import sys
sys.stdin = open('input.txt')

def pre_order(T):
    if T:
        print(T, end=' ')
        pre_order(left[T])
        pre_order(right[T])

N = int(input())
E = N-1
arr = list(map(int, input().split()))
left = [0] * (N+1) # 부모를 인덱스로 왼쪽 자식번호 저장
right = [0] * (N+1)
par = [0] * (N+1) # 자식을 인덱스로 부모 저장

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    # 아래처럼 입력해도 됨
    # for i in range(0, E*2, 2):
    #     p, c = arr[i], arr[i+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = N
while par[c] != 0: # 부모가 있으면
    c = par[c]
root = c
print(root)
pre_order(root)