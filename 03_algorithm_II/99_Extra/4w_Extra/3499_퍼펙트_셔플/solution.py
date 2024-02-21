import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    cards = input().split()

    if N % 2 == 0:
        deq1 = cards[:N//2]
        deq2 = cards[N//2:]
    else:
        deq1 = cards[:N//2+1]
        deq2 = cards[N//2+1:]

    result = []
    while True:
        if deq1:
            result.append(deq1.pop(0))
        if deq2:
            result.append(deq2.pop(0))
        if not deq1 and not deq2:
            break

    print(f'#{test_case}', *result)