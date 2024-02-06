import sys
sys.stdin = open('input.txt')

def brute_force(pattern, target):
    pattern_idx = 0
    target_idx = 0
    # 현재 조사 위치가 조사대상의 범위를 벗나가기 전까지
    while target_idx < len(target):
        # 일치하지 않으면
        if pattern[pattern_idx] != target[target_idx]:
            pattern_idx = -1
            target_idx -= pattern_idx
        target_idx += 1
        pattern_idx += 1
        # 패턴의 끝까지 index 증가
        # = target과 pattern이 일치하지 않는 부분 없이 패턴의 끝까지 조사
        if pattern_idx == len(pattern):
            return True
    # 패턴을 끝까지 찾았지만 없을 때
    return False

def KMP(pattern, target):
    lps = make_lps(pattern, target)
    pattern_idx = 0
    target_idx = 0
    # 현재 조사 위치가 조사대상의 범위를 벗나가기 전까지
    # print(lps)
    while target_idx < len(target):
        # print(lps[pattern_idx])
        # print(target_idx, target[target_idx], pattern_idx, pattern[pattern_idx])
        # 일치하지 않으면
        if pattern[pattern_idx] != target[target_idx]:
            pattern_idx = lps[pattern_idx]
        target_idx += 1
        pattern_idx += 1
        # 패턴의 끝까지 index 증가
        # = target과 pattern이 일치하지 않는 부분 없이 패턴의 끝까지 조사
        if pattern_idx == len(pattern):
            return True
    # 패턴을 끝까지 찾았지만 없을 때
    return False

# 내 앞에 나와 동일한 패턴이 몇번 나왔는지를 세어주는 리스트
def make_lps(pat, tar):
    lps = [0] * (len(pat) + 1)
    for idx in range(1, len(pat)):
        if pat[lps[idx-1]] == pat[idx]:
            lps[idx] = lps[idx - 1] + 1
    lps.insert(0, -1)
    return lps

def boyer_moore(pattern, target):
    lps = {pattern[idx] : len(pattern)-1-idx for idx in range(len(pattern))} # 스킵 가능한 범위 기록
    pattern_idx = len(pattern)
    target_idx = 0

    while target_idx <= len(target) - pattern_idx:
        for p_idx in range(pattern_idx-1, -1,- 1):
            if target[target_idx + p_idx] != pattern[p_idx]:
                target_idx += lps.get(target[target_idx + p_idx], len(pattern))
                break
        else:
            return True
    return False

T = int(input())

for test_case in range(1, T+1):
    str1 = input()
    str2 = input()

    result = brute_force(str1, str2)
    print(f'#{test_case} {int(result)}')

    result2 = KMP(str1, str2)
    print(f'#{test_case} {int(result2)}')

    result3 = boyer_moore(str1, str2)
    print(f'#{test_case} {int(result3)}')