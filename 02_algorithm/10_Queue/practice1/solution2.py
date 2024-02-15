N = 10
# 큐 생성
Q = [0] * N
front = rear = -1

rear += 1 # enQueue(1)
Q[rear] = 1
rear += 1
Q[rear] = 2
rear += 1
Q[rear] = 3

while front != rear: # duQueue()
    front += 1
    print(Q[front])