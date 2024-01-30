import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    ai = int(input())

    counts = [0 for _ in range(10)]

    num = 0
    count = 0

    # counts 리스트 작성
    for i in range(N):
        counts[ai % 10] += 1
        ai //= 10

    # counts 리스트 순회하면서 가장 높은 수(카드가 많은 인덱스) 탐색
    for i in range(len(counts)-1, -1, -1):
        # 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력
        if counts[i] == max(counts):
            num = i
            count = counts[i]
            break

    print(f'#{test_case} {num} {count}')

# 방법2
'''
    T = int(input())

    for tc in range(1, T+1):
        N = int(input())
        ai = list(map(int, input()))
        
        counting_list = [0 for _ in range(10)]
        
        for num in ai:
            counting_list[num] += 1
            
        max_count = 0 # 보유 개수
        result = 0  # 카드 번호
        
        for i in range(10):
            if max_count <= counting_list[i]:
                max_count = counting_list[i]
                result = i
                
        print(f'#{tc} {result} {max_count}')
'''