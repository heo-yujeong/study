import sys
sys.stdin = open('input.txt')

N = int(input())

num_list = [list(map(int, input().split())) for _ in range(N)]

result = 0
for num in num_list:
    result += sum(num)

print(result)

# 방법 2
result = 0
for numbers in num_list:
    for num in numbers:
        result += num
print(result)