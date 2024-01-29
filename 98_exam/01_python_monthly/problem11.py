############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def get_final_position(N, matrix, move_list):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                result = [i, j] # matrix를 모두 순회하면서 처음 위치를 찾음
    
    # 0 ~ 3번 이동하는 동안 리스트의 값에 변화를 줄 dx, dy
    # resutl[x, y]
    # 예) 0번 이동 => result[x-1, y+0]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for move in move_list: # 리스트에 있는 이동을 진행하는 동안
        result[0] += dx[move] # move번 이동 = dx[move], dy[move] 만큼 이동
        result[1] += dy[move]
        if 0 <= result[0] < N and 0 <= result[1] < N: # 이동 후 x, y좌표 위치가 모두 0~N 사이이면
            continue # result(좌표)를 그대로 출력하기 위해 pass
        else:
            return None # 한번이라도 벗어나면 None을 반환하고 함수 종료

    return result


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
N = 3
matrix = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
] 
moves1 = [1, 1, 3]
print(get_final_position(N, matrix, moves1)) # [2, 1]

moves2 = [1, 2, 3, 3]
print(get_final_position(N, matrix, moves2)) # None
#####################################################
