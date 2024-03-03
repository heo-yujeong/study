import sys
sys.stdin = open('input.txt')

dx = [0, 0, -0.5, 0.5]
dy = [0.5, -0.5, 0, 0]

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    atom_lst = [list(map(int, input().split())) for _ in range(N)]
    hap_eng = 0

    while len(atom_lst) >= 2:
        new_atom_lst = []
        is_crash = {}

        for atom in atom_lst:
            atom[0] += dx[atom[2]]
            atom[1] += dy[atom[2]]
            if -1000 <= atom[0] <= 1000 and -1000 <= atom[1] <= 1000:
                key = (atom[0], atom[1])
                if key in is_crash:
                    is_crash[key].append(atom)
                else:
                    is_crash[key] = [atom]

        for atoms_at_pos in is_crash.values():
            if len(atoms_at_pos) >= 2:
                for atom in atoms_at_pos:
                    hap_eng += atom[3]
            else:
                new_atom_lst.append(atoms_at_pos[0])

        atom_lst = new_atom_lst

    print(f'#{test_case} {hap_eng}')