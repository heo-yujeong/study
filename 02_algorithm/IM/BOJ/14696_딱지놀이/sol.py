import sys
sys.stdin = open('input.txt')

N = int(input())

for _ in range(N):
    A = input().split()[1:]
    B = input().split()[1:]

    if A.count('4') == B.count('4') and A.count('3') == B.count('3') and A.count('2') == B.count('2') and A.count('1') == B.count('1'):
        print('D')
    else:
        if A.count('4') > B.count('4'):
            print('A')
        elif A.count('4') == B.count('4'):
            if A.count('3') > B.count('3'):
                print('A')
            elif A.count('3') == B.count('3'):
                if A.count('2') > B.count('2'):
                    print('A')
                elif A.count('2') == B.count('2'):
                    if A.count('1') > B.count('1'):
                        print('A')
                    else:
                        print('B')
                else:
                    print('B')
            else:
                print('B')
        else:
            print('B')