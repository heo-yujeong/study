a = 1
b = 2

def enclosed():
	a = 10 # 로컬에 새로운 변수로 선언
	c = 3

	def local(c):
		print(a, b, c) # 10 2 500

	local(500)
	print(a, b, c) # 10 2 3

enclosed()
print(a, b) # 1 2

'''
global_var = 100
def local():
	print(global_var)
	global_var += 3
	print(global_var) # UnboundLocalError: local variable 'global_var' referenced before assignment
	# local에서 들어있는 값을 확인하는 것은 가능하지만, 값을 바꿀 수는 없음
	# global_var = 3 으로 재정의 하는 것은 가능!
local()
'''

global_list = [1, 2, 3]
def local2():
	global_list[0] = 100 # 이건 왜 가능? 리스트는 참조하는 것이라서 리스트의 0번째 위치의 참조 값을 100으로 바꾼 것
	# 참조하는 리스트는 그대로, 0번째의 주소값에 존재하는 값만 바뀌는 것이라 바꿀 수 있음 
	print(global_list)
	
local2() # [100, 2, 3]


# 함수로 글로벌 스코프에 정의된 변수의 값을 바꾸는 법
# 1. 재할당하기!
global_var2 = 100
def local3(parm):
	parm += 3
	return parm

global_var2 = local3(global_var2)
print(global_var2)

# 2. global 키워드 사용
# 어느 시점에 변수의 값이 바뀌었는지 알기 어렵기 때문에 익숙해지기 전까지는 1번 방법으로 사용하기!
global_var3 = 100
def local4():
	global global_var3
	global_var3 += 3

local4()
print(global_var3)