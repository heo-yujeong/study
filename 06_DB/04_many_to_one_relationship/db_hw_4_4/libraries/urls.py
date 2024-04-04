from django.urls import path
from . import views


app_name = 'libraries'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_pk>/', views.detail, name='detail'),
    path('<int:book_pk>/create_review/', views.create_review, name='create_review'),
    path('<int:book_pk>/review/<int:review_pk>/delete_review/', views.delete_review, name='delete_review'),
]
