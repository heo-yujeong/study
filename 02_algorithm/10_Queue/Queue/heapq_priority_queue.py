from queue import PriorityQueue
import heapq

# priority queue
q = PriorityQueue()
q.put((45, 'z')) # 우선순위가 높다 = 수가 작다
q.put((17, 'x')) # 우선순위 = 정수의 오름차순 기준
print(q.queue)


# heapq # 완전 이진트리
arr= [(45, 'z'), (17, 'x'), (6, 'a'), (100, 'b')]
heapq.heapify(arr) # 최소 힙 => 우선순위가 낮은 요소가 부모 노드
print(arr)

heapq.heappush(arr, (4, 't'))
print(arr)

heapq.heappush(arr, (30, 'f'))
print(arr)

heapq.heappop(arr)
print(arr)