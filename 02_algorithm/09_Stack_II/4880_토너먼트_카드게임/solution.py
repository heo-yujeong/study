import sys
sys.stdin = open('input.txt')

def div_group(start, end):
    # 한명만 남으면 게임할 필요 X
    if start == end:
        return start

    # 반으로 나누는 작업 반복
    # i ~ (i+j)//2
    # (i+j)//2+1 ~ j
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

# 테스트케이스 수
T = int(input())

for test_case in range(1, T+1):
    # 학생 수
    N = int(input())
    # 각 학생의 카드 번호
    card = list(map(int, input().split()))

    # 학생 순서 = 인덱스 번호 + 1
    result = div_group(0, N-1) + 1

    print(f'#{test_case} {result}')