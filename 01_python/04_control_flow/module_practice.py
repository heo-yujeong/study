# 모듈 : 함수를 모아놓은 파일
# 모듈 불러오기
import random
# 같은 디렉토리에 random.py가 있다면 해당 파일을 불러온다.
# 없으면 파이썬 라이브러리의 random을 찾아온다

print(random.sample(range(1, 46), 6)) # sample : 비복원 추출(반복되지 않는 수 뽑기)

'''
모듈을 가져온다 == 해당 파일 위~아래 까지 실행하는 것 == 해당 파일을 가져온 곳에 복붙한 것!
파일 안에 print로 적혀있던 것은 읽는 순간 다 출력하고 시작!

import하기 전에는 해당 모듈 쓸 수 없음
import는 최상단에 쓰는게 좋아
import 하는 순서
    1. core : 시스템을 건드는 모듈 (os, sys)
    2. built-in : 파이썬 모듈
    3. 3rd party library : 다른 사람이 만들어 둔 모듈(request, notebook)

pprint 모듈 : 데이터 양식 맞춰서 정리해서 프린트!

모듈들의 모임(폴더) = 패키지  => pip install이 필요
'''