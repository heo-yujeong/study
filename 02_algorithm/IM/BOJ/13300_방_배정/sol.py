import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
man = [0] * 7
wom = [0] * 7

for _ in range(N):
    gender, grade = map(int, input().split())

    if gender == 1:
        man[grade] += 1
    else:
        wom[grade] += 1

cnt = 0
for i in range(len(man)):
    if man[i] % K == 0:
        cnt += man[i] // K
    else:
        cnt += man[i] // K + 1

    if wom[i] % K == 0:
        cnt += wom[i] // K
    else:
        cnt += wom[i] // K + 1

print(cnt)