from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from django.conf import settings
from .serializers import WeatherSerializer
from .models import Weather

api_key = settings.WHETHER_API_KEY

# Create your views here.
def index(request):
    city_name = 'Seoul,KR'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'

    response = requests.get(url).json()
    return JsonResponse(response)

def save_data(request):
    city_name = 'Seoul,KR'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'

    response = requests.get(url).json()
    for li in response.get('list'):
        dt_txt = li.get('dt_txt')
        temp = li.get('main').get('temp')
        feels_like = li.get('main').get('feels_like')

        # print(dt_txt, temp, feels_like)
        save_data = {
            'dt_txt': dt_txt,
            'temp': temp,
            'feels_like': feels_like,
        }
        serializer = WeatherSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    return JsonResponse({'message': 'save okay'})


@api_view(['GET'])
def list_data(request):
    weathers = Weather.objects.all()
    serializers = WeatherSerializer(weathers, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def hot_weathers(request):
    # weathers = Weather.objects.all()
    # hot_weathers = []
    # for weather in weathers:
    #     celsius = round(weather.temp - 273.15, 2)
    #     if celsius > 20:
    #         hot_weathers.append(weather)
    # serializers = WeatherSerializer(hot_weathers, many=True)

    # 권장방식
    weathers = Weather.objects.filter(temp__gt=(20+273.15))
    serializers = WeatherSerializer(weathers, many=True)
    return Response(serializers.data)