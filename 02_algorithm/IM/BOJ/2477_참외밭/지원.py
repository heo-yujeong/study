import sys
sys.stdin = open('input.txt')

# 참외의 개수
K = int(input())

# 육각형의 변에 대한 정보
direction = []

# 육각형의 변에 대한 정보를 입력받고 리스트에 저장합니다.
for _ in range(6):
    N, M = map(int, input().split())  # N은 동서남북, M은 변의 길이
    direction.append([N, M])

sou_nor = []
eas_wes = []

for i in range(6):
    if direction[i][0] == 3 or direction[i][0] == 4:
        sou_nor.append(direction[i][1])
    elif direction[i][0] == 1 or direction[i][0] == 2:
        eas_wes.append(direction[i][1])

max1 = max(sou_nor)
max2 = max(eas_wes)

my_road1 = 0
my_road2 = 0
for i in range(6):
    if direction[i][1] == max2:
        max_index2 = i # 세로로 제일 김

for i in range(6):
    if direction[i][1] == max1:
        max_index1 = i # 가로로 제일 김

# 양 옆에 없는 값을 찾습니다.
for i in range(6):  # 남,북에서 가장 긴 변
    if direction[i][0] == 1 or direction[i][0] == 2:
        if max_index1 == 0:
            my_road1 = direction[3][1]
        elif max_index1 == 1:
            my_road1 = direction[4][1]
        elif max_index1 == 2:
            my_road1 = direction[5][1]
        elif max_index1 == 3:
            my_road1 = direction[0][1]
        elif max_index1 == 4:
            my_road1 = direction[1][1]
        elif max_index1 == 5:
            my_road1 = direction[2][1]

for i in range(6):  # 동,서에서 가장 긴 변
    if direction[i][0] == 3 or direction[i][0] == 4:
        if max_index2 == 0:
            my_road2 = direction[3][1]
        elif max_index2 == 1:
            my_road2 = direction[4][1]
        elif max_index2 == 2:
            my_road2 = direction[5][1]
        elif max_index2 == 3:
            my_road2 = direction[0][1]
        elif max_index2 == 4:
            my_road2 = direction[1][1]
        elif max_index2 == 5:
            my_road2 = direction[2][1]


area = ((max1 * max2) - (my_road1 * my_road2)) * K
print(area)