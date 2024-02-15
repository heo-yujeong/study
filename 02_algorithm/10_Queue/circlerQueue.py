N = 10
cQ = [0] * N
front = rear = -1

# 삽입
def enQueue(item):
    global rear
    if isFull():
        print('Queue_Full')
    else:
        rear = (rear + 1) % len(cQ)
        cQ[rear] = item

# 삭제
def deQueue():
    global front
    if isEmpty():
        print('Queue_Empty')
    else:
        front = (front + 1) % len(cQ)
        return cQ[front]

# 공백상태 검사
def isEmpty():
    return front == rear

# 포화상태 검사
def isFull():
    return (rear + 1) % len(cQ) == front