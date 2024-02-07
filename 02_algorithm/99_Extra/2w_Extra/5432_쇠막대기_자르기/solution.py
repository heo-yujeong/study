import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    laser_bar = input()

    result = 0 # 잘린 개수
    bar = 0 # 쇠막대 수

    for i in range(len(laser_bar)):
        if laser_bar[i] == '(':
            bar += 1
        else:
            bar -= 1

            if laser_bar[i-1] == '(' : # 레이저 였다면
                result += bar
            else:
                result += 1

    print(f'#{test_case} {result}')