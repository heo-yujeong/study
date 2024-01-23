# 자동으로 .git 폴더 삭제 해주는 코드
# 현재 폴더를 기준으로 모든 폴더를 조사하여서 .git 폴더 삭제
# 단, 코드가 실행된 위치의 .git은 제외!
import os # os 파이썬 표준 라이브러리 : 운영체제와 상호작용 가능
import subprocess # 다른 프로세스를 통해 실행 시킨다!

# print(os.getcwd()) # get current working directory
# os.chdir('01_python/') # working directory 변경

current_folder = os.getcwd()

# 현재 폴더 및 모든 하위 폴더에서 반복
for foldername, subfolders, filenames in os.walk(current_folder):
    # print(foldername) # 폴더 경로
    # print(subfolders) # 하위 폴더(들)
    # print(filenames) # 하위 폴더(들)
    if '.git' in subfolders: # 하위폴더 목록에 .git이 있으면
        if foldername == current_folder: # root 디렉토리는 제외
            continue
        git_folder_path = os.path.join(foldername, '.git') # 삭제하려는 .git폴더의 위치를 변수에 저장
        subprocess.run(['rm', '-rf', git_folder_path])
        print(f'{git_folder_path} 폴더가 삭제되었습니다.')