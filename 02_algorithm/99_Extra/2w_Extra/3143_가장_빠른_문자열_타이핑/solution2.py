import sys
sys.stdin = open('input.txt')

# 브루트 포스
def brute_force(pattern, text):
    txt_idx = 0
    pat_idx = 0

    cnt = 0

    while txt_idx < len(text):
        if text[txt_idx] != pattern[pat_idx]:
            txt_idx -= pat_idx
            pat_idx = -1
        txt_idx += 1
        pat_idx += 1

        if pat_idx == len(pattern):
            cnt += 1
            pat_idx = 0

    return cnt


# KMP
def KMP(pattern, text):
    lps = make_lps(pattern)
    txt_idx = 0
    pat_idx = 0

    cnt = 0

    while txt_idx < len(text):
        if text[txt_idx] != pattern[pat_idx]:
            pat_idx = lps[pat_idx]
        txt_idx += 1
        pat_idx += 1

        if pat_idx == len(pattern):
            cnt += 1
            pat_idx = 0

    return cnt

def make_lps(pat):
    lps = [0] * (len(pat) + 1)
    for idx in range(1, len(pat)):
        if pat[lps[idx]] == pat[idx]:
            lps[idx] = lps[idx-1] + 1
    lps[0] = -1
    return lps


# 보이어 무어
def boyer_moore(pattern, text):
    lps = {pattern[idx]: max(1,len(pattern)-1-idx) for idx in range(len(pattern))}
    print(lps)
    txt_idx = 0
    pat_idx = len(pattern)

    cnt = 0

    while txt_idx <= len(text) - pat_idx:
        for p_idx in range(pat_idx-1, -1, -1):
            if text[txt_idx + p_idx] != pattern[p_idx]:
                txt_idx += lps.get(text[txt_idx + p_idx], len(pattern))
                break
        else:
            cnt += 1
            txt_idx += len(pattern)

    return cnt


T = int(input())

for test_case in range(1, T+1):
    A, B = input().split()

    # cnt_brute = brute_force(B, A)
    # cnt_kmp = KMP(B, A)
    cnt_boy = boyer_moore(B, A)
    # result = len(A) - (cnt_brute * len(B)) + cnt_brute
    # result = len(A) - (cnt_kmp * len(B)) + cnt_kmp
    result = len(A) - (cnt_boy * len(B)) + cnt_boy

    print(f'#{test_case} {result}')