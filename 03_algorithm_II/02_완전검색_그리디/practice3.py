card = list(map(int, input().split()))
path = []
used = [0] * 6
is_bbg = False

def is_baby_gin():
    if (path[0]+1 == path[1] and path[1]+1 == path[2]) or (path[0] == path[1] == path[2]):
        if (path[3]+1 == path[4] and path[4]+1 == path[5]) or (path[3] == path[4] == path[5]):
            return True
    return False

def perm(lev):
    global is_bbg
    if lev == len(card):
        if is_baby_gin():
            is_bbg = True
        return

    for i in range(6):
        if used[i]:
            continue
        used[i] = True
        path.append(card[i])
        perm(lev+1)
        path.pop()
        used[i] = False

perm(0)
if is_bbg:
    print('Yes')
else:
    print('No')