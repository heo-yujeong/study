import sys
from itertools import permutations
sys.stdin = open('input2.txt', encoding='UTF-8')

N = int(input())
S, P = map(int, input().split())
scores = {}
# 팀번호 : [[학생1점수, 학생1정확도, 학생1언어구분, 학생1이름],
#           [학생2점수, 학생2정확도, 학생2언어구분, 학생2이름],
#           점수 평균, 강사님과 점수 차]

for i in range(1, N+1):
    stu1 = input().split()
    stu2 = input().split()
    scores[i] = [stu1, stu2]

# 강사님 점수
teach_score = S * P * 0.01

# 개인별 점수
for k, v in scores.items():
    score = 0
    for i in range(2):
        if v[i][2] == 'K':
            score += int(int(v[i][0]) * int(v[i][1]) * 0.01 * 0.7)
        else:
            score += int(int(v[i][0]) * int(v[i][1]) * 0.01)
    score = score // 2
    scores[k].append(score)

    per_score = []

    for per in permutations(str(score) if score > 99 else '0'+str(score)):
        per_score.append(int(abs(teach_score-int(''.join(per)))))
    scores[k].append(min(per_score))


# 결과
result = [] # 팀번호, 이름1, 이름2, 점수평균(원점수), 강사님과의 차이
for k, v in scores.items():
    result.append([k, v[0][3], v[1][3], v[2], v[3]])

result.sort(key=lambda x:(x[4], -x[3]))

for i in range(len(result)):
    print(f'{i+1}등 : {result[i][1]} {result[i][2]} ({result[i][0]} 팀) | 점수 차 : {result[i][4]} | 원점수 : {result[i][3]}')