# 문자열 뒤집기
import sys
sys.stdin = open('input.txt')

s1 = input()
print('전 :', s1)

s1 = s1[::-1]
print('후 :', s1)
print()

s2 = input()
print('전 :', s2)
s2 = list(s2)
s2.reverse()
s2 = ''.join(s2)
print('후 :', s2)