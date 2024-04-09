# 필요 기술 스택
- python
- django == 4.2.x
- ~~bootstrap~~

# 개발 환경
- VSCode

# 프로젝트 구성
1. 프로젝트명 : crud
2. accounts app
  - 인증 기능(회원가입, 로그인, 로그아웃)
  - 프로필 페이지
  - 팔로우 기능
3. articles app
  - 게시글 CRUD + 작성자 정보
  - 좋아요 기능

# 기능별 사용자 요청 경로
1. accounts urls
   => BASE_URL : https://localhost/accounts/
   | 기능 | method | url | view 함수(매개변수) |
   |---|---|---|---|
   | 회원가입 페이지 보여주기 | GET | /signup/ | signup |
   | 회원정보 생성 | POST | /signup/ | signup |
   | 로그인 페이지 보여주기 | GET | /login/ | login |
   | 로그인 기능(session 생성) | POST | /login/ | login |
   | 로그아웃 기능(session 삭제) | POST | /logout/ | logout |
   | 프로필 페이지 | GET | /{str:username}/ | profile (username) |
   | 팔로우 버튼 렌더링 페이지 | GET | /{str:username}/ | profile (username) |
   | 팔로우 기능 | POST | /{int:profile_owner_pk}/ | follow (profile_owner_pk) |

2. articles urls
   => BASE_URL : https://localhost/articles/
   | 기능 | method | url | view 함수(매개변수) | 제약 조건 |
   |---|---|---|---|---|
   | 메인 페이지 | GET | '' | index | pk 기준 내림차순 정렬 |
   | 게시글 생성 페이지 | GET | /create/ | create | 로그인 필요 |
   | 게시글 생성 기능 | POST | /create/ | create | 로그인 필요 |
   | 게시글 수정 페이지 | GET | /{int:article_pk}/update/ | update | 로그인 필요, 작성자인 경우 |
   | 게시글 수정 기능 | POST | /{int:article_pk}/update/ | update | 로그인 필요, 작성자인 경우 |
   | 게시글 삭제 기능 | POST | /{int:article_pk}/delete/ | delete | 로그인 필요, 작성자인 경우 |
   | 좋아요 버튼 렌더링 페이지 | GET | '' | index | 로그인 필요, 작성자가 아닌 경우 |
   | 좋아요 기능 | POST | /{int:article_pk}/like/ | like (article_pk) | 로그인 필요, 작성자가 아닌 경우 |

# 설정
1. 한글, 한국 시간
2. base 템플릿 사용
   - nav bar 각종 링크들 추가
3. app별 template 폴더 규칙
  - app/templates/app/*.html
  - app/templates/assets/*.css
  - app/templates/assets/*.png