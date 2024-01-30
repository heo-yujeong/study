import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input()) # 버스 노선 개수
    bus_info = list(list(map(int, input().split())) for _ in range(N)) # 버스노선 정보
    P = int(input()) # 정류장 개수
    C = [int(input()) for _ in range(P)] # 정류장 번호

    # bus_dict = {} # 정류장 번호를 키로 하는 딕셔너리 생성(초기 value는 0으로)
    # for station in C:
    #     bus_dict[station] = 0
    #
    # for bus in bus_info: # 버스 노선 정보가 있는 동안 반복
    #     for i in range(bus[0], bus[1]+1): # 버스 노선이 지나는 동안 result[정류장 번호] +1
    #         if bus_dict.get(i) != None:
    #             bus_dict[i] += 1
    #
    # result = []
    # for c in C:
    #     result.append(bus_dict[c])
    #
    # print(f'#{test_case}', *result)

    # 방법2
    counts = [0] * P

    for bus in bus_info:
        for i in range(len(C)):
            if bus[0] <= C[i] <= bus[1]:
                counts[i] += 1

    print(f'#{test_case}', *counts)