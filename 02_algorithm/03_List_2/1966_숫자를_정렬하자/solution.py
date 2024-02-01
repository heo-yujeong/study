import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    # 1. 기본 sort
    num_list.sort()

    print(f'#{test_case}', *num_list)

    # 2. 버블 정렬
    '''
    for i in range(N-1, 0, -1):
        for j in range(N-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

    print(f'#{test_case}', *num_list)
    '''

    # 3. 카운팅 정렬
    '''    
    sorted_num_list = [0] * len(num_list)
    counts = [0] * (max(num_list) + 1)

    for num in num_list:
        counts[num] += 1

    for i in range(1, len(counts)):
        counts[i] = counts[i-1] + counts[i]

    for i in range(len(sorted_num_list)-1, -1, -1):
        counts[num_list[i]] -= 1
        sorted_num_list[counts[num_list[i]]] = num_list[i]

    print(f'#{test_case}', *sorted_num_list)
    '''

    # 4. 선택 정렬
    '''
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if num_list[min_idx] > num_list[j]:
                min_idx = j
        num_list[min_idx], num_list[i] = num_list[i], num_list[min_idx]

    print(f'#{test_case}', *num_list)
    '''