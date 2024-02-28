# 회의실 배정
# 최대한 많은 횟수의 회의가 되도록

req = [(5, 9), (6, 10), (8, 11), (1, 4), (3, 5), (1, 6), (5, 7), (3, 8), (2, 13), (12, 14)]
req.sort(key=lambda x:(x[1], x[0]))

cnt = 1
time = req[0][1]

for start, end in req:
    if start >= time:
        cnt += 1
        time = end

print(cnt)