# 화장실 대기시간들의 총 합
person = [15, 30, 50, 10]
person.sort()

hap = 0
# for i in range(len(person)):
#     hap += person[i] * (len(person)-(i+1))
#
# print(hap)

# 강사님 코드
n = len(person)
left_person = n-1
for turn in range(n):
    time = person[turn]
    hap += left_person * time
    left_person -= 1

print(hap)