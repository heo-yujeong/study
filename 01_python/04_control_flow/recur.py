# 재귀함수로 팩토리얼 구현
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))

# while문으로 팩토리얼 구현
def fact_while(n):
    result = 1

    while n > 1:
        result *= n
        n -= 1

    return result

print(fact_while(5))

# for문으로 팩토리얼 구현
def fact_for(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

print(fact_for(5))


# 피보나치 수열
def fibo(n):
    if n <= 1 :
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
print(fibo(5))

# while문으로 피보나치 수열
def fibo_while(n):
    pass

# for문으로 피보나치 수열
def fibo_for(n):
    pass