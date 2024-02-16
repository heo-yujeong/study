import sys
sys.stdin = open('input2.txt')

N = int(input()) # 기둥 개수
dot_height = []
for _ in range(N):
    w, h = map(int, input().split())
    dot_height.append([w, h])

sorted_height = sorted(dot_height, key=lambda x: x[0])
print(sorted_height)
max_height =  max(sorted_height, key=lambda x: x[1])[1]

rocations = [roc[0] for roc in sorted_height if roc[1] == max_height]
print(rocations)

result = 0
for i in range(sorted_height[0][0], 8):
    print(i)