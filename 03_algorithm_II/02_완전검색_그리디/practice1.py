# 3개의 주사위 눈금의 합이 10 이하인 것만 출력
path = []
cnt = 0

# def kfc(x, sum):
#     if x == 3:
#         if sum <= 10:
#             print(f'{path} = {sum}')
#         return
#
#     for i in range(1, 7):
#         path.append(i)
#         kfc(x+1, sum+i)
#         path.pop()
#
# kfc(0, 0)
# 위는 모든 가지를 다 탐색하기 때문에 비효율적

# 따라서 아래처럼 가지치기 추가
def kfc1(x, sum):
    global cnt
    if sum > 10:  # 가지치기
        return

    if x == 3:
        # print(f'{path} = {sum}')
        cnt += 1


    for i in range(1, 7):
        path.append(i)
        kfc1(x+1, sum+i)
        path.pop()

kfc1(0, 0)
print(cnt)