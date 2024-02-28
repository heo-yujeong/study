import sys
sys.stdin = open('input.txt')

def change(arr, cnt):
    global result
    # 출력결과 때문에 저장을 이렇게..
    temp = ''
    for number in arr:
        temp += number

    # 이미 이전에 만들어졌던 조합이면 pass
    # 만들어지지 않은 조합이면 result리스트의 남은 교환횟수 번째에 append
    if temp in result[cnt]:
        return
    else:
        result[cnt].append(temp)

    # 교환횟수가 남아있지 않으면 함수 종료
    if cnt == 0:
        return

    # 숫자를 하나씩 선택하면서 자리 교환 => 조합을 만듦
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            change(arr, cnt-1)
            arr[i], arr[j] = arr[j], arr[i] # 자리 되돌리기

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # 숫자판 정보, 교환 횟수
    board, num = input().split()
    # 숫자판을 리스트화
    board = list(board)

    # 교환 횟수마다 만들 수 있는 조합을 담을 리스트
    result = [[] for _ in range(int(num)+1)]
    # 교환하는 함수(인자: 숫자판, 남은 교환 횟수)
    change(board, int(num))

    # 마지막 교환 => 리스트의 0번에 append됨
    # 가장 큰 금액 = 그 중에서 가장 큰 값
    print(f'#{test_case} {max(result[0])}')