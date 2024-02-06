import sys
sys.stdin = open('input.txt')

def f(patt, txt, m, n):
    for i in range(n-m+1): # text에서 비교 시작 위치
        for j in range(M):
            if txt[i+j] != patt[j]:
                break
        else:
            return 1
    # 모든 위치에서 비교가 끝난 경우
    return 0

T = int(input())

for tc in range(1, T+1):
    pat = input()
    text = input()
    M = len(pat)
    N = len(text)

    ans = f(pat, text, M, N)
    print(f'#{tc} {ans}')