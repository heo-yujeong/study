import sys
sys.stdin = open('input.txt')

def rotate_number(num16):
    return num16[-1] + num16[:-1]

def create_number(num16):
    set_num = set()
    for i in range(4):
        set_num.add(num16[i*N//4:i*N//4+N//4])
    return set_num

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    num_16 = input()
    cre_num = set()

    for i in range(4):
        cre_num.add(num_16[i*N//4:i*N//4+N//4])

    for i in range(N//4-1):
        num_16 = rotate_number(num_16)
        set_16 = create_number(num_16)
        cre_num.update(set_16)

    cre_num10 = []
    for num in cre_num:
        cre_num10.append(int(num, base=16))
    cre_num10.sort(reverse=True)
    print(f'#{test_case} {cre_num10[K-1]}')