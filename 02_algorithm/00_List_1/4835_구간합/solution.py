import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    num_list  = list(map(int, input().split()))

    hap_list = []
    for i in range(N-M+1):
        hap = 0
        for j in range(i, i+M):
            hap += num_list[j]
        hap_list.append(hap)
    print(f'#{test_case} {max(hap_list)-min(hap_list)}')