import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    for _ in range(N):
        a, b = map(int(input().split()))