import sys
sys.stdin = open('input.txt')

# 입력이 있는만큼 계속 반복
while True:
    try:
        # 테스트 케이스
        test_case = int(input())
        # 8개의 수 입력
        arr = list(map(int, input().split()))

        # 반복문 종료를 위한 check 변수
        check = False

        # 종료조건이 있을 때까지 반복
        while True:
            # 한 사이클 => 5회
            for i in range(1, 6):
                # 가장 첫번째 숫자에 1~5를 순서대로 뺌
                num = arr.pop(0) - i
                # 종료조건
                # num가 0보다 작거나 같을 때
                # 가장 마지막 자리에 0을 넣고 종료
                if num <= 0:
                    arr.append(0)
                    check = True
                    break
                # 종료조건에 해당하지 않으면 마지막 자리에 계산된 값 입력
                arr.append(num)
            if check:
                break

        # 암호 출력
        print(f'#{test_case}', *arr)
    except:
        break