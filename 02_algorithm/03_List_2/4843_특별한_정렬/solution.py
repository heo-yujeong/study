import sys
sys.stdin = open('input.txt')

# 1. N 개의 정수를 오름차순으로 정렬
# 2. 해당 인덱스가 짝수이면 가장 마지막 인덱스의 값 출력
# 2-1. 홀수이면 가장 앞 인덱스의 값 출력

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    # 1. 기본 정렬
    ai.sort()

    result = []

    for i in range(len(ai)):
        if i % 2 == 0:
            result.append(ai.pop())
        else:
            result.append(ai.pop(0))

    print(f'#{test_case}', *result)

    # 2. 버블 정렬
    '''
    for i in range(N-1, 0, -1):
        for j in range(i):
            if ai[j] > ai[j+1]:
                ai[j], ai[j+1] = ai[j+1], ai[j]
    
    result = []

    for i in range(len(ai)):
        if i % 2 == 0:
            result.append(ai.pop())
        else:
            result.append(ai.pop(0))

    print(f'#{test_case}', *result)
    '''

    # 3. 카운팅 정렬
    '''
    sort_ai = [0] * len(ai) # 0 ~ max(ai) 까지 리스트
    counts = [0] * (max(ai) + 1)

    for i in range(len(ai)):
        counts[ai[i]] += 1

    for i in range(1, len(counts)):
        counts[i] = counts[i-1] + counts[i] # 누적합

    for i in range(len(sort_ai)-1, -1, -1):
        counts[ai[i]] -= 1
        sort_ai[counts[ai[i]]] = ai[i]

    result = []

    for i in range(len(ai)):
        if i % 2 == 0:
            result.append(sort_ai.pop())
        else:
            result.append(sort_ai.pop(0))

    print(f'#{test_case}', *result)
    '''

    # 4. 선택 정렬
    '''
    for i in range(len(ai)-1):
        min_idx = i
        for j in range(i+1, len(ai)):
            if ai[min_idx] > ai[j]:
                min_idx = j
        ai[min_idx], ai[i] = ai[i], ai[min_idx]
        
    result = []

    for i in range(len(ai)):
        if i % 2 == 0:
            result.append(ai.pop())
        else:
            result.append(ai.pop(0))

    print(f'#{test_case}', *result)
    '''