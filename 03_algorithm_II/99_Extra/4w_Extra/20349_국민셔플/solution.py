import sys
sys.stdin = open('input.txt')

TC = int(input())

for test_case in range(1, TC+1):
    N, T = map(int, input().split())
    card = [i for i in range(1, N+1)]

    for _ in range(T):
        card = card[N-int(N*0.37):] + card[:N-int(N*0.37)]

        left = card[:N-int(N*0.5):]
        right = card[N-int(N*0.5):]

        card = []
        while True:
            if left:
                card.append(left.pop(0))
            if right:
                card.append(right.pop(0))
            if not left and not right:
                break

    print(f'#{test_case}', *card)