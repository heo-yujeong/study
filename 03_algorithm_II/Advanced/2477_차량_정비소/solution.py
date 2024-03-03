import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    tk = list(enumerate(map(int, input().split()), 1))

    a = [0] * N
    b = [0] * M

    a_select = {}
    b_select = {}

    b_wait = []
    time = tk[0][1]
    while True:
        if not tk and len(b_wait) == K:
            break
        while 0 in a:
            if tk == []:
                break
            if tk and tk[0][1] <= time:
                idx = a.index(0)
                a[idx] = ai[idx]
                if a_select.get(idx+1, None) != None:
                    a_select[idx+1].append(tk[0][0])
                else:
                    a_select[idx+1] = [tk[0][0]]
                tk.pop(0)
            if tk and tk[0][1] > time:
                break
        time += 1
        for i in range(len(a)):
            a[i] -= 1
            if a[i] == -1:
                a[i] = 0
                continue
            if a[i] == 0:
                b_wait.append([a_select[i+1][-1], time])

    end = []
    time = b_wait[0][1]
    while True:
        if not b_wait and len(end) == K:
            break
        while 0 in b:
            if b_wait == []:
                break
            if b_wait and b_wait[0][1] <= time:
                idx = b.index(0)
                b[idx] = bj[idx]
                if b_select.get(idx+1, None) != None:
                    b_select[idx+1].append(b_wait[0][0])
                else:
                    b_select[idx+1] = [b_wait[0][0]]
                b_wait.pop(0)
            if b_wait and b_wait[0][1] > time:
                break

        time += 1
        for i in range(len(b)):
            b[i] -= 1
            if b[i] == -1:
                b[i] = 0
                continue
            if b[i] == 0:
                end.append([b_select[i+1][-1], time])

    hap = -1
    if a_select.get(A, 0) != 0 and b_select.get(B, 0) != 0:
        a_lst = []
        b_lst = []
        a_lst += a_select[A]
        b_lst += b_select[B]
        hap_lst = set(a_lst).intersection(set(b_lst))
        if len(hap_lst):
            hap = sum(hap_lst)

    print(f'#{test_case} {hap}')