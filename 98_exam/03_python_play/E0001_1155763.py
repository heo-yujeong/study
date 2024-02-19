import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'SEOUL01_PYTHON'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.



    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    targets = []
    if balls[1][0] != -1:
        targets.append([balls[1][0], balls[1][1]])
    if balls[3][0] != -1:
        targets.append([balls[3][0], balls[3][1]])
    if balls[5][0] != -1:
        targets.append([balls[5][0], balls[5][1]])    
    targetBall_x = targets[0][0]
    targetBall_y = targets[0][1]


    # 사분면 결정
    def spaceSelect(whiteBall_x, whiteBall_y, targetBall_x, targetBall_y):
        if whiteBall_x < targetBall_x:
            if whiteBall_y < targetBall_y:
                return 1
            else:
                return 4
        else:
            if whiteBall_y < targetBall_y:
                return 2
            else:
                return 3      
    
    # 홀 결정
    # HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]
    def holeSelect(space, whiteBall_x, whiteBall_y, targetBall_x, targetBall_y):
        # 1 사분면일 경우
        if space == 1:
            if targetBall_x > 127:
                return 254, 127
            else:
                return 127, 127
        elif space == 2:
            if targetBall_x > 127:
                return 127, 127
            else:
                return 0, 127
        elif space == 3:
            if targetBall_x > 127:
                return 127, 0
            else:
                return 0, 0
        else:
            if targetBall_x > 127:
                return 254, 0
            else:
                return 127, 0

    # angle 계산
    if whiteBall_x == targetBall_x:
        if whiteBall_y < targetBall_y:
            angle = 0
        else:
            angle = 180
    elif whiteBall_y == targetBall_y:
        if whiteBall_x < targetBall_x:
            angle = 90
        else:
            angle = 270
    else:
        space = spaceSelect(whiteBall_x, whiteBall_y, targetBall_x, targetBall_y)
        hole_x, hole_y = holeSelect(space, whiteBall_x, whiteBall_y, targetBall_x, targetBall_y)

        if space == 1:
            # 흰-홀 각도 > 흰-타 각도
            wh_ho = math.degrees(math.atan(abs(hole_x-whiteBall_x)/abs(whiteBall_y-hole_y)))
            wh_ta = math.degrees(math.atan(abs(targetBall_x-whiteBall_x)/abs(whiteBall_y-targetBall_y)))
            if wh_ho > wh_ta:
                radian_a = math.atan(abs(targetBall_x-whiteBall_x)/abs(whiteBall_y-hole_y))
                angle = math.degrees(radian_a)
            elif wh_ho < wh_ta:
                radian_a = math.atan(abs(whiteBall_y-targetBall_y)/abs(hole_x-whiteBall_x))
                angle = 90 - math.degrees(radian_a)
            else:
                angle = wh_ho
        elif space == 2:
            # 흰-홀 각도 > 흰-타 각도
            wh_ho = math.degrees(math.atan(abs(whiteBall_x-hole_x)/abs(whiteBall_y-hole_y)))
            wh_ta = math.degrees(math.atan(abs(whiteBall_x-targetBall_x)/abs(whiteBall_y-targetBall_y)))
            if wh_ho > wh_ta:
                radian_a = math.atan(abs(whiteBall_x-targetBall_x)/abs(whiteBall_y-hole_y))
                angle = 360 - math.degrees(radian_a)
            elif wh_ho < wh_ta:
                radian_a = math.atan(abs(whiteBall_y-targetBall_y)/abs(whiteBall_x-hole_x))
                angle = 271 + math.degrees(radian_a)
            else:
                angle = 270 + wh_ta
        elif space == 3:
            # 흰-홀 각도 > 흰-타 각도
            wh_ho = math.degrees(math.atan(abs(hole_y-whiteBall_y)/abs(whiteBall_x-hole_x)))
            wh_ta = math.degrees(math.atan(abs(targetBall_y-whiteBall_y)/abs(whiteBall_x-targetBall_x)))
            if wh_ho > wh_ta:
                radian_a = math.atan(abs(targetBall_y-whiteBall_y)/abs(whiteBall_x-hole_x))
                angle = 270 - math.degrees(radian_a)
            elif wh_ho < wh_ta:
                radian_a = math.atan(abs(whiteBall_x-targetBall_x)/abs(hole_y-whiteBall_y))
                angle = 180 + math.degrees(radian_a)
            else:
                angle = 270 - wh_ho
        else:
            # 흰-홀 각도 > 흰-타 각도
            wh_ho = math.degrees(math.atan(abs(hole_y-whiteBall_y)/abs(hole_x-whiteBall_x)))
            wh_ta = math.degrees(math.atan(abs(targetBall_y-whiteBall_y)/abs(hole_x-whiteBall_x)))
            if wh_ho > wh_ta:
                radian_a = math.atan(abs(whiteBall_y-targetBall_y)/abs(hole_x-whiteBall_x))
                angle = 93 + math.degrees(radian_a)
            elif wh_ho < wh_ta:
                radian_a = math.atan(abs(targetBall_x-whiteBall_x)/abs(hole_y-whiteBall_y))
                angle = 180 - math.degrees(radian_a)
            else:
                angle = 90 + wh_ho

    width = abs(targetBall_x - whiteBall_x)
    height = abs(targetBall_y - whiteBall_y)
    distance = math.sqrt(width**2 + height**2)
    power = distance * 0.5
        
    

    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    # 
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')