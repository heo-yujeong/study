import sys
sys.stdin = open('input.txt')

number = int(input())

result = 0
for i in range(1, number+1):
    result += i

print(result)