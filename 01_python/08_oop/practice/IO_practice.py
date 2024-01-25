# 0001.숫자의 입력과 출력
# # 방법 1
# num1 = int(input())
# num2 = int(input())

# print(num1 + num2)

# # 방법 2
# result = 0
# for i in range(2):
#     result += int(input())

# print(result)


# 0007.2차원 List의 전체 합 구하기
import sys
# text 파일의 각 줄을 input 함수가 실행될 때마다 넣어줌
sys.stdin = open('input.txt')

# 방법 1
# N = int(input())
# result = []
# for i in range(N):
#     arr = input().split()
#     digit_list = []
#     for num in arr:
#         digit_list.append(int(num))
#     result.append(digit_list)
# print(result)

# 방법 2
# N = int(input())
# result = []
# for i in range(N):
#     arr = list(map(int, input().split()))
#     result.append(arr)
# print(result)

# 방법 3
N = int(input())
result = [list(map(int, input().split())) for _ in range(N)]
print(result)