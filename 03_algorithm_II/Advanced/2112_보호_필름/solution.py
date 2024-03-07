import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    # 두께, 가로크기, 합격 기준
    D, W, K = map(int, input().split())
    # A: 0, B: 1
    film = [list(map(int, input().split())) for _ in range(D)]

    '''
    성능검사하는 함수
    인자 (합격기준 k, 투입횟수 cnt)
    return 합격 여부
    음... 함수 이상한뎁....
    return 투입 횟수
      열우선탐색 => 한 줄이라도 없으면 바로 멈춤!
      + 투입횟수 1 해서 다시 탐색
    투입횟수 0일때
    세로를 확인하면서 각 줄에 합격기준개의 같은것이 있는지 확인
    투입횟수 1일때 => 0번째 줄부터 1 or 0 넣어보기
    출력 결과 : 성능검사를 통과할 수 있는 약품의 최소 투입 횟수



    함수 2개 필요한거같은뎁
    함수 1.
    dfs하듯이 cnt == max되면 멈추고....
    어디를 바꿀지 체크
    위에 바꿨다가 함수 돌려보고 바꾼거 해제

    함수 2.
    성능검사 통과 가능한지 체크
    (몇번째 줄 바꾸는지 체크해서 함수 ㄱ)
    return true false
    '''
    '''
    다 필요없이 하나의 함수로 체크하게 만들어볼까..
    '''