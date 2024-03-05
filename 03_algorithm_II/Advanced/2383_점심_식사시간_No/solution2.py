import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    floor = [list(map(int, input().split())) for _ in range(N)]

    time = 1

    '''
    모든 경우의 수 만들어서 탐색해보기
    1. 모든 사람이 1번 계단을 선택한 경우
    2. 1번은 2번 계단, 나머지는 1번 계단
    ...
    
    n. 모든 사람이 2번 계단을 선택한 경우
    
    최대값을 지정해두고 가지치기
    
    DP...? 끄아아아아앙....
    '''

    print(f'#{test_case} {time}')