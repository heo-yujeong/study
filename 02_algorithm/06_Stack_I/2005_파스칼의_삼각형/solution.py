import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    result = []

    for i in range(N):
        num = []
        for j in range(i+1):
            if i == j or j == 0:
                num.append(1)
            else:
                num.append(result[i-1][j-1] + result[i-1][j])
        result.append(num)

    print(f'#{test_case}')
    for res in result:
        print(*res)