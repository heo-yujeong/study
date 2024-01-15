print('-' * 20, '변수 사용 X', '-' * 20)
print('3의 2배 :', 3 * 2)
print('3의 제곱 값 :', 3 ** 2)
print('3의 제곱 값을 3의 2배의 값으로 나눈 몫 :', (3 ** 2) // (3 * 2),' 나머지 :', (3 ** 2) % (3 * 2))
print('3의 제곱 값에 -3의 제곱 값을 더한 값 :',3 ** 2 + (-3) ** 2)

print('-' * 20, '변수 사용 O', '-' * 20)

two_multiples_of_three = 3 * 2
three_squared = 3 ** 2
minus_three_squared = (-3) ** 2

print('3의 2배 :', two_multiples_of_three)
print('3의 제곱 값 :', three_squared)
print('3의 제곱 값을 3의 2배의 값으로 나눈 몫 :', three_squared // two_multiples_of_three,' 나머지 :', three_squared % two_multiples_of_three)
print('3의 제곱 값에 -3의 제곱 값을 더한 값 :',three_squared + minus_three_squared)