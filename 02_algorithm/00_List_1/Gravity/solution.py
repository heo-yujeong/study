import sys
sys.stdin = open('input.txt')

N = int(input()) # 상자가 쌓여있는 가로 길이
arr = list(map(int, input().split()))

max_v = 0 # 가장 큰 낙차를 저장할 변수

for i in range(N-1): # 낙차를 구할 위치
	cnt = 0 # 자기자신보다 오른쪽에 있는 상자 중 낮은 상자 개수
	for j in range(i+1, N): # i와 비교할 위치
		if arr[i] > arr[j]:
			cnt += 1
	if max_v < cnt:
		max_v = cnt

print(max_v)