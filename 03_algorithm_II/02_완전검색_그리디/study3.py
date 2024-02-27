# branch = 2, level = 3 인 재귀함수 만들어 보기
def run(level):
    if level == 3:
        return

    for i in range(2):
        run(level+1)

print(0)