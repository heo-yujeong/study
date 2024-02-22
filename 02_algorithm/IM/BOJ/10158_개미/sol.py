import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x_pm = (p + t) // w
y_pm = (q + t) // h

if x_pm % 2 == 0:
    x = (p + t) % w
else:
    x = w - (p + t) % w

if y_pm % 2 == 0:
    y = (q + t) % h
else:
    y = h - (q + t) % h

print(x, y)