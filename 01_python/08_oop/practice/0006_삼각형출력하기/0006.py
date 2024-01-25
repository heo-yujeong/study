import sys
sys.stdin = open('input.txt')

number = int(input())

for i in range(1, number+1):
    print('*' * i)


# 방법 2
for i in range(1, number+1):
    for j in range(i):
        print('*', end='')
    print()