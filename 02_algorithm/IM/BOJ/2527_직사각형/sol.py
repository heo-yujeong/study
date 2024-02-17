import sys
sys.stdin = open('input.txt')

while True:
    try:
        x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

        result = 'a'
        if x1 == p2 or x2 == p1 or y1 == q2 or y2 == q1:
            result = 'b'
        if (x1 == p2 and y1 == q2) or (p1 == x2 and y1 == q2) or (p1 == x2 and q1 == y2) or (x1 == p2 and q1 == y2):
            result = 'c'
        if p1 < x2 or q1 < y2 or p2 < x1 or q2 < y1:
            result = 'd'

        print(result)

    except:
        break