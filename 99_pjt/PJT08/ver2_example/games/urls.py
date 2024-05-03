from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start),
    path('guess/<int:session_id>/', views.guess),
]
