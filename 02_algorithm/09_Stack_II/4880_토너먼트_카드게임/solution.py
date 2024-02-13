import sys
sys.stdin = open('input.txt')

def div_group(start, end):
    if start == end:
        return start

    one = div_group(start, (start+end)//2)
    other = div_group((start+end)//2+1, end)
    return play(one, other)

def play(peo1, peo2):
    # 1: 가위, 2: 바위, 3: 보
    if card[peo1] == card[peo2]:
        return peo1
    elif card[peo1] - card[peo2] in [-2, 1]:
        return peo1
    else:
        return peo2

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))

    result = div_group(0, N-1) + 1

    print(f'#{test_case} {result}')