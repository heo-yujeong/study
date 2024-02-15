# 클래스로 큐 구현하기
class Queue:
    def __init__(self, maxsize):
        self.size = maxsize
        self.items = [None] * maxsize
        self.rear = -1
        self.front = -1

    def enQueue(self, item):
        self.rear += 1
        self.items[self.rear] = item

    def deQueue(self):
        self.front += 1
        return self.items[self.front]

q = Queue(3)
q.enQueue('a')
q.enQueue('b')
q.enQueue('c')
print(q.items)
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())