def enqueue(n): # 삽입
    global last
    # 마지막 노드 추가
    last += 1
    # 마지막 노드에 데이터(키) 삽입
    h[last] = n
    # 부모 > 자식 조건이 만족하도록 교환 반복
    c = last # 자식 노드 번호
    p = c // 2 # 부모 노드 번호
    while p and  h[p] < h[c]:
    # 부모노드가 있는데, 부모 노드 값이 자식 노드 값보다 작을 때
        h[p], h[c] = h[c], h[p]
        c = p
        p = c // 2

def dequeue(): # 삭제
    global last
    # 루트 노드 원소 삭제
    # => 키가 가장 큰 값이 삭제됨(다꺼내면 내림차순?)
    tmp = h[1] # 루트의 키 값 보관
    h[1] = h[last]
    last -= 1
    p = 1 # 새로 옮긴 루트
    c = p * 2
    while c <= last: # 자식이 있으면
        if c + 1 <= last and h[c] < h[c+1]: # 오른쪽 자식이 더 크면
            c += 1
        if h[p] < h[c]:
            h[p], h[c] = h[c], h[p]
            p = c
            c = p * 2
        else:
            break
    return tmp



N = 10
h = [0] * (N+1) # (최대)힙

# 2 5 3 6 4 순으로 삽입
last = 0 # 힙의 마지막 노드 번호

enqueue(2)
enqueue(5)
enqueue(3)
enqueue(6)
enqueue(4)
print(h)
# 힙이 빌때까지 dequeue 수행
while last > 0:
    print(dequeue())