import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    height_n = list(map(int, input().split()))
    result = 0
    #
    # for i in range(2, N-2):
    #     height = height_n[i]
    #     if height_n[i-2] < height and height_n[i-1] < height and height_n[i+1] < height and height_n[i+2] < height:
    #         result += height - max([height_n[i-2], height_n[i-1], height_n[i+1], height_n[i+2]])
    #
    # print(f'#{test_case} {result}')


    # 방법 2
    '''
    for i in range(2, N-2):
        min_value = 256 # 건물 최대 높이 : 255
        for j in range(5):
            if j != 2:
                if height_n[i] - height_n[i-2+j] < min_value:
                    min_value = height_n[i] - height_n[i-2+j] # i가 가지는 조망권 최대값
        if min_value > 0:
            result += min_value
            
    print(f'#{test_case} {result}')
    '''

    # 방법 3
    '''
    for i in range(2, N-2):
        max_neighbor = 0
        for j in range(i-2, i+3):
            if i == j:
                continue
            if height_n[j] < height_n[i] and max_neighbor < height_n[j]:
                max_neighbor = height_n[j]
            elif height_n[j] >= height_n[i]:
                max_neighbor = height_n[i]
                break
        result += height_n[i] - max_neighbor
        
    print(f'#{test_case} {result}')
    '''