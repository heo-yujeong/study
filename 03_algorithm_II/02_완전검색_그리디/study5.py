# 중복순열과 순열 구현
# N개의 주사위를 던져 ㅇ나올 수 있는 모든 중복순열과 순열을 출력
'''
[입력]
2 1
[출력]
1 1
1 2
...
6 5
6 6
'''
def type1(x):
    if x == N:
        print(path)
        return

    for i in range(1, 7):
        path.append(i)
        type1(x+1)
        path.pop()

def type2(x):
    if x == N:
        print(path)
        return

    for i in range(1, 7):
        if used[i]:
            continue
        used[i] = True
        path.append(i)
        type2(x+1)
        path.pop()
        used[i] = False

path = []
used = [False for _ in range(7)]
N, type = map(int, input().split())

if type == 1:
    print('중복순열')
    type1(0)
if type == 2:
    print('순열')
    type2(0)