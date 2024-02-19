import sys
sys.stdin = open('input.txt')

N = int(input())
pick_num = input().split()

line = []
for i in range(1, len(pick_num)+1):
    if i == 1:
        line.append(i)
    elif i == 2:
        if pick_num[i-1] == 0:
            line.append(i)
        else:
            line.insert(0, i)
    else:
        if pick_num[i-1] == 0:
            line.append(i)
        else:
            line.insert(i-int(pick_num[i-1])-1, i)

print(*line)