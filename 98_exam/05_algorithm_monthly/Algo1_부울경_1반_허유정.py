# import sys
# sys.stdin = open('algo1_sample_in.txt')

# 16진수 -> 2진수
hex_to_bin = {hex(num)[2:].upper(): f'{num:04b}' for num in range(16)}
# 2진수 -> 16진수
bin_to_hex = {f'{num:04b}': f'{num:x}'.upper() for num in range(16)}

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # n: 자릿수, numbers: 2진수 or 16진수의 수
    n, numbers = input().split()
    # 24자리의 2진수가 입력된다면
    if len(numbers) == 24:
        print(f'#{test_case}', end=' ')
        for i in range(0, len(numbers)-1, 4):
            # 4자리씩 끊어서 2진수를 16진수로 출력
            print(bin_to_hex[numbers[i:i+4]], end='')
        print()
    # 6자리의 16진수가 입력된다면
    else:
        print(f'#{test_case}', end=' ')
        # 하나의 16진수에 대응하는 2진수를 출력
        for num in numbers:
            print(hex_to_bin[num], end='')
        print()