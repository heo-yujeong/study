import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    # N: 피자의 개수, M: 화덕에 한번에 넣을 수 있는 피자 수
    N, M = map(int, input().split())
    # N개의 피자 => 값은 치즈의 양
    pizza = list(map(int, input().split()))
    # [피자 번호, 치즈의 양] 순서쌍으로
    num_pizza = []
    for idx, cheeze in enumerate(pizza):
        num_pizza.append([idx+1, cheeze])

    # 1번부터 순서대로 피자를 화덕에 넣음
    # oven = 현재 화덕에 있는 피자
    oven = num_pizza[:N]
    # remain = 남아있는 피자
    remain = num_pizza[N:]

    # 화덕에 마지막 피자 1개만 남아있을 때까지
    while len(oven) > 1:
        # 가장 앞의 피자를 꺼내서 치즈의 양을 반으로 줄임
        cheeze = oven.pop(0)
        cheeze[1] //= 2
        # 치즈가 0이 되면 remain의 가장 앞에 있는 피자를 화덕에 넣음
        # => remain에 피자가 있을 때까지만
        # 치즈가 다 녹지 않으면 다시 oven에 넣어줌
        if cheeze[1] == 0:
            if remain:
                oven.append(remain.pop(0))
        else:
            oven.append(cheeze)

    # 마지막에 남아있는 피자 = oven의 0번 인덱스
    # 저장된 피자 = [피자 번호, 치즈의 양] 순서
    print(f'#{test_case} {oven[0][0]}')