from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('todos/', views.index, name='index'),
    path('todos/create_todo/', views.create_todo, name='create_todo'),
    path('todos/<work>/', views.detail, name='detail'),
]