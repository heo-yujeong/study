import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    height_n = list(map(int, input().split()))
