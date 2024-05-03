from django.shortcuts import render
from django.http import JsonResponse
import random

from .models import GameSession

# Create your views here.
def start(request):
    target_number = random.randint(1, 100)
    game_session = GameSession.objects.create(target_number=target_number)
    context = {
        'target_number': target_number,
        'session_id': game_session.id,
    }
    return render(request, 'game.html', context)

def guess(request, session_id):
    game_session = GameSession.objects.get(pk=session_id)
    user_guess = int(request.POST.get('user_guess'))

    message = '정답입니다!'
    if(user_guess < 1 or user_guess > 100):
        message = '1 ~ 100 사이 숫자만 입력하세요!'
    elif(user_guess > game_session.target_number):
        message = 'DOWN!'
        game_session.user_guess = user_guess
        game_session.attempts += 1
        game_session.save()
    elif(user_guess < game_session.target_number):
        message = 'UP!'
        game_session.user_guess = user_guess
        game_session.attempts += 1
        game_session.save()
    
    context = {
        'message': message,
        'attempts': game_session.attempts,
        'is_correct': user_guess == game_session.target_number,
    }
    return JsonResponse(context)