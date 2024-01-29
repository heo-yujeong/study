import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    height_n = list(map(int, input().split()))
    result = 0

    for i in range(2, N-2):
        height = height_n[i]
        if height_n[i-2] < height and height_n[i-1] < height and height_n[i+1] < height and height_n[i+2] < height:
            result += height - max([height_n[i-2], height_n[i-1], height_n[i+1], height_n[i+2]])

    print(f'#{test_case} {result}')