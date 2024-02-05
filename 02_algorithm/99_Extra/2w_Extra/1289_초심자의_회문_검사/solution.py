import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    word = list(input())
    palin = [0] * len(word)
    result = 0 # 회문이면 1

    for i in range(len(word)):
        palin[-i-1] = word[i]

    if word == palin:
        result = 1

    print(f'#{test_case} {result}')