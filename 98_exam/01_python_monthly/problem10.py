############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_position_safe(N, M, current):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    result = True # 제한 구역을 넘어가지 않는다고 가정
    current = list(current) # 튜플은 값을 변화시킬 수 없어 리스트로 변경
    # 0 ~ 3번 이동하는 동안 리스트의 값에 변화를 줄 dx, dy
    # current[x, y]
    # 예) 0번 이동 => current[x-1, y+0]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    current[0] += dx[M] # M번 이동 = dx[M], dy[M] 만큼 이동
    current[1] += dy[M]

    if 0 <= current[0] < N and 0 <= current[1] < N: # 이동 후 x, y좌표 위치가 모두 0~N 사이이면
        pass # result를 그대로 출력하기 위해 pass
    else:
        result = False # result르 False로 변환(제한 구역을 넘어감)

    return result


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(is_position_safe(3, 1, (0, 0))) # True
print(is_position_safe(3, 0, (0, 0))) # False
#####################################################
