from queue import Queue

q = Queue()
print(q)

q.put('a')
q.put('b')
q.put('c')
print(q.queue)
print(q.qsize())
print(q.get())
print(q.queue)

# 멀티스레드 프로그래밍
q2 = Queue(3)
q2.put('a')
q2.put('b')
q2.put('c')
print(q2.queue)
q2.put('d') # 코드가 멈춘것이 아니라 대기 상태
# 이미 큐는 full 상태이기 때문에 처리 끝내지 못함