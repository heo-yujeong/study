import sys
sys.stdin = open('input.txt')

number = int(input())

for i in range(number+1):
    print(number-i)

# 방법 2
for i in range(number, -1, -1):
    print(i)