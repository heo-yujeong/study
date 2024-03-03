import sys
sys.stdin = open('input.txt')

# 상하좌우
dx = [0, 0, -0.5, 0.5]
dy = [0.5, -0.5, 0, 0]

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    atom_lst = [list(map(int, input().split())) for _ in range(N)]
    hap_eng = 0

    while len(atom_lst) >= 2:
        for i in range(len(atom_lst)):
            atom_lst[i][0] += dx[atom_lst[i][2]]
            atom_lst[i][1] += dy[atom_lst[i][2]]

        is_crash = {}
        for atom in atom_lst:
            if is_crash.get((atom[0], atom[1]), 0) != 0:
                is_crash[(atom[0], atom[1])].append(atom)
            else:
                is_crash[(atom[0], atom[1])] = [atom]

        atom_lst = []

        for (x, y) in is_crash:
            if len(is_crash[(x, y)]) >= 2:
                for atom in is_crash[(x, y)]:
                    hap_eng += atom[3]
            else:
                if -1000 <= is_crash[(x, y)][0][0] <= 1000 and -1000 <= is_crash[(x, y)][0][1] <= 1000:
                    atom_lst.append(is_crash[(x, y)][0])
    print(f'#{test_case} {hap_eng}')