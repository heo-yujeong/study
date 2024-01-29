import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    n_dict = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}

    for n in n_dict.keys():
        while N % n == 0:
            n_dict[n] += 1
            N //= n
    print(f'#{test_case} {n_dict[2]} {n_dict[3]} {n_dict[5]} {n_dict[7]} {n_dict[11]}')
