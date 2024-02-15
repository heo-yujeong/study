# 큐 구현
# 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
# 큐에서 세 개의 데이터를 차례로 꺼내서 출력
# 출력 예시 : 1, 2, 3

queue = []
queue.append(1)
queue.append(2)
queue.append(3)
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))
while queue:
    print(queue.pop(0))