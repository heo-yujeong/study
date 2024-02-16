import sys
sys.stdin = open('input2.txt')

while True:
    try:
        x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    except:
        break