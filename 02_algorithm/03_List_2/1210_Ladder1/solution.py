import sys
sys.stdin = open('input.txt')

for _ in range(10):
    test_case = int(input())
    mat = [list(map(int, input().split())) for _ in range(100)]

