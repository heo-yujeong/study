import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 버스 노선 개수
    counts = [0] * 5001 # 5000번 정류장까지 count배열

    for i in range(N):
        # 각 버스 노선이 들리는 정류장번호( A ~ B 까지)
        # 1 <= A <= B <= 5000
        A, B = map(int, input().split())
        # A와 B 사이에 있는 정류장 번호의 인덱스에 해당하면 +1
        for j in range(A, B+1):
            counts[j] += 1
    P = int(input()) # 정류장 개수
    busstop = [int(input()) for _ in range(P)] # 정류장 번호

    print(f'#{tc}', end= ' ')
    for i in busstop: # 버스정류장 번호를 하나씩 순회
        # 그때 번호에 해당하는 counts인덱스의 값 출력
        print(counts[i], end= ' ')
    print()