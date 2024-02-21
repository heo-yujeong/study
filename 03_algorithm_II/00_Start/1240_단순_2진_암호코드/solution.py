import sys
sys.stdin = open('input.txt')

code = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9
}
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    password = []
    result = 0

    for _ in range(N):
        line = input()
        if int(line) != 0:
            line = str(int(line[::-1]))
            line = line[:56][::-1]

            for i in range(0, 56, 7):
                password.append(code[line[i:i + 7]])

            result_pw = password[:8]
            hap = 0
            for i in range(len(result_pw)):
                if i % 2 == 0:
                    hap += result_pw[i] * 3
                else:
                    hap += result_pw[i]
            if hap % 10 == 0:
                result = sum(result_pw)

    print(f'#{test_case} {result}')