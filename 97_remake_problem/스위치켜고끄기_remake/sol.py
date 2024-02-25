import sys
sys.stdin = open('input.txt')

def isSosu(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    switch = [None] + list(map(int, input().split()))
    num_stu = int(input())
    sosu_list = []
    for i in range(1, N+1):
         if isSosu(i):
             sosu_list.append(i)

    for _ in range(num_stu):
        gender, number = map(int, input().split())

        if gender == 1: # 남학생 => 소수
            if number in sosu_list:
                for sosu in sosu_list:
                    for i in range(sosu-number, sosu+number+1):
                        if 0 < i <= N:
                            switch[i] = 1 - switch[i]

        else: # 여학생 => 약수
            yaksu = []
            for i in range(1, number + 1):
                if number % i == 0:
                    yaksu.append(i)
            for num in yaksu:
                switch[num] = 1 - switch[num]

    print(f'#{tc}')
    for i in range(1, len(switch)):
        print(switch[i], end=' ')
        if i % 20 == 0:
            print()
    print()