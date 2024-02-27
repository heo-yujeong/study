import sys
sys.stdin = open('input.txt')

def isBbj(arr):
    counts = [0] * 10
    for num in arr:
        counts[num] += 1
    for i in range(len(counts)):
        if counts[i] >= 3:
            return 1
    for i in range(len(counts)-2):
        if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
            return 1
    return 0

T = int(input())

for test_case in range(1, T+1):
    cards = list(map(int, input().split()))
    play1 = []
    play2 = []
    result = 0

    for _ in range(6):
        play1.append(cards.pop(0))
        play2.append(cards.pop(0))

        if isBbj(play1) > isBbj(play2):
            result = 1
            break
        elif isBbj(play1) < isBbj(play2):
            result = 2
            break

    print(f'#{test_case} {result}')