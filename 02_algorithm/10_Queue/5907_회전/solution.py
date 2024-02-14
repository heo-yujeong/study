import sys
sys.stdin = open('input.txt')

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # N: 수열 길이, M: 반복할 작업 횟수
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        arr.append(arr.pop(0))

    print(f'#{test_case} {arr[0]}')