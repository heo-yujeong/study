import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    num_pizza = []
    for idx, cheeze in enumerate(pizza):
        num_pizza.append([idx+1, cheeze])

    oven = num_pizza[:N]
    remain = num_pizza[N:]

    while len(oven) > 1:
        cheeze = oven.pop(0)
        cheeze[1] //= 2
        if cheeze[1] == 0:
            if remain:
                oven.append(remain.pop(0))
        else:
            oven.append(cheeze)

    print(f'#{test_case} {oven[0][0]}')