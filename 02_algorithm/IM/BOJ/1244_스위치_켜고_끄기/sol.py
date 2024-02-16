import sys
sys.stdin = open('input.txt')

num_swc = int(input()) # 스위치 개수
swc = list(map(int, input().split())) # 스위치 상태
# 1: 켜짐, 0: 꺼짐
num_stu = int(input()) # 학생 수

for _ in range(num_stu):
    # 학생 성별, 받은 번호
    # 1: 남학생, 2: 여학생
    morw, number = map(int, input().split())

    # 남학생이면
    # 번호의 배수번째 있는 스위치 상태 바꿈
    if morw == 1:
        for i in range(len(swc)):
            if (i+1) % number == 0:
                swc[i] = 1 - swc[i]

    # 여학생이면
    # 좌우대칭인 부분에 속하는 모든 스위치 바꿈
    else:
        # 뽑은 번호 값 바꿈
        swc[number-1] = 1 - swc[number-1]
        idx = 1
        while True:
            # 범위를 벗어나면 멈춤
            if number - 1 - idx < 0 or number - 1 + idx > len(swc) - 1:
                break
            # 뽑은 번호를 기준으로 양 옆이 같은지 확인
            if swc[number-1-idx] == swc[number-1+idx]:
                # 같으면 번호 바꿔줌
                swc[number-1-idx] = 1 - swc[number-1-idx]
                swc[number-1+idx] = 1 - swc[number-1+idx]
                idx += 1
            # 양 옆이 같지 않으면 break
            else:
                break

cnt = 0
for s in swc:
    if cnt != 0 and cnt % 20 == 0:
        print()
    cnt += 1
    print(s, end=' ')