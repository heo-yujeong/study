from django.shortcuts import render

# Create your views here.
# 메인 페이지를 만드는 index라는 이름의 함수
def index(request):
    return render(request, 'index.html')