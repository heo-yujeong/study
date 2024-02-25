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
    arr = sorted(list(set(list(input() for _ in range(N)))))
    arr.pop(0)
    password = []
    result = 0

    for line in arr:
        line = line.rstrip('0')[::-1][:56][::-1]
        for i in range(0, 56, 7):
            password.append(code[line[i : i+7]])

        hap = 0
        for i in range(8):
            if i % 2 == 0:
                hap += password[i] * 3
            else:
                hap += password[i]
        if hap % 10 == 0:
            result = sum(password)

    print(f'#{test_case} {result}')