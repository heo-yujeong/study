import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

num1, num2 = map(int, input().split())
print(num1 + num2)
print(num1 * num2)