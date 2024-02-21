import sys
sys.stdin = open('input.txt')

# 최소힙에 값 입력
def enqueue(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    # 부모 노드가 있고, 부모 노드의 값이 자식 노드의 값보다 크면
    while p and heap[p] > heap[c]:
        # 값을 바꿔줌
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

# 테스트케이스
T = int(input())

for test_case in range(1, T+1):
    # 노드의 개수
    N = int(input())
    # 최소 힙
    heap = [0] * (N+1)
    # 힙의 마지막 노드 번호
    last = 0

    # 최소힙에 저장할 숫자 리스트
    order = list(map(int, input().split()))
    # 숫자를 차례대로 최소힙에 저장
    for num in order:
        enqueue(num)

    # 조상 노드의 정수 합 저장
    hap = 0
    while True:
        # 조상 노드 인덱스 = 현재 노드의 인덱스 // 2
        last //= 2
        # 조상 노드가 존재하면 더해줌
        if last > 0:
            hap += heap[last]
        # 존재하지 않으면 반복 종료
        else:
            break

    print(f'#{test_case} {hap}')