import sys
sys.stdin = open('input.txt')

pattern = [[2, 1, 1], [2, 2, 1], [1, 2, 2], [4, 1, 1], [1, 3, 2],
           [2, 3, 1], [1, 1, 4], [3, 1, 2], [2, 1, 3], [1, 1, 2]]

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = sorted(list(set(list(input().strip() for _ in range(N)))))
    arr.pop(0)
    result = 0
    check = []

    for i in range(len(arr)):
        hex_to_bin = ''
        for j in range(len(arr[i])):
            hex_to_bin += f'{int(arr[i][j], base=16):04b}'
        hex_to_bin = hex_to_bin.rstrip('0')

        password = []
        cnt1 = cnt2 = cnt3 = cnt4 = 0
        for x in range(len(hex_to_bin)-1, -1, -1):
            if hex_to_bin[x] == '1' and cnt3 == 0:
                cnt4 += 1
            elif hex_to_bin[x] == '0' and cnt2 == 0:
                cnt3 += 1
            elif hex_to_bin[x] == '1' and cnt1 == 0:
                cnt2 += 1
            elif hex_to_bin[x] == '0':
                if hex_to_bin[x-1] == '1' or not hex_to_bin[x-1]:
                    cnt = min(cnt2, cnt3, cnt4)
                    password.append(pattern.index([cnt2//cnt, cnt3//cnt, cnt4//cnt]))
                    cnt2 = cnt3 = cnt4 = 0
                    if len(password) == 8:
                        hap = 0
                        for k in range(len(password)):
                            if k % 2 == 0:
                                hap += password[k]
                            else:
                                hap += password[k] * 3
                        if hap % 10 == 0:
                            if password not in check:
                                result += sum(password)
                                check.append(password)
                        password = []

    print(f'#{test_case} {result}')