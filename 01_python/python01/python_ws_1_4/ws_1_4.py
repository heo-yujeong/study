# 원주율
3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# 반지름
15

PI = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
radius = 15

PI_is = '원주율 : '
radius_is = '반지름 : '
round_is = '원의 둘레 : '
area_is = '원의 넓이 : '

print(f'{PI_is}{PI}')
print(f'{radius_is}{radius}')
print(f'{round_is}{radius * 2 * PI}')
print(f'{area_is}{radius * radius * PI}')