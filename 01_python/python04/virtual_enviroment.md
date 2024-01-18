# 가상환경 설정
=> 현재 프로젝트를 위한 환경설정을 위해

- 방법
```bash
# 대체로 폴더명은 venv로 작성
$ python -m venv {폴더명}
# 가상환경 활성화
$ source venv/Scripts/Activate
# 사용할 외부 라이브러리 설치
$ pip install requests
# 패키지 목록 확인
$ pip list
# 활성화된 가상환경에 설치된 패키지 목록만 기록
$ pip freeze > requirements.txt
# 가상환경 종료
$ deactivate

# requirements.txt에 기록된 패키지 설치
$ pip install -r requirements.txt
```