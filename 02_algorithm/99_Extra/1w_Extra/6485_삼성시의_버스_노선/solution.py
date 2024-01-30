import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input()) # 버스 개수
    arr = [map(int, input().split()) for _ in range(N)]
    P = int(input()) # 정류장 개수
    C = [int(input()) for _ in range(P)] # 정류장 번호

