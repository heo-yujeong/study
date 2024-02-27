# 11 12 13 21 22 23 31 32 33까지 출력하는 코드
for a in range(1,4):
    for b in range(1, 4):
        print(a, b)


# 1111 1112 ~ 3332 3333까지 출력하는 코드
for a in range(1, 4):
    for b in range(1, 4):
        for c in range(1, 4):
            for d in range(1, 4):
                print(a, b, c, d)
# 위는 1~4까지 모든 수를 선택하는 경우와 같음 => '중복'순열

# 위의 내용을 중복순열로 구현
path = []
N = 3

def run(lev):
    if lev == N:
        print(path)
        return

    for i in range(1, 4):
        path.append(i)
        run(lev+1)
        path.pop()

run(0)