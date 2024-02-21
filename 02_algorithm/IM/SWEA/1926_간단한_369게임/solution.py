import sys
sys.stdin = open('input.txt')

N = int(input())
num = list(map(str, range(1, N+1)))

for i in range(len(num)):
    if '3' in num[i] or '6' in num[i] or '9' in num[i]:
        num[i] = '-' * (num[i].count('3') + num[i].count('6') + num[i].count('9'))

print(*num)