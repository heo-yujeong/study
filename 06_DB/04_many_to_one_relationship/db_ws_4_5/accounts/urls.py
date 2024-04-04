from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update, name='update'),
    path('<int:user_pk>/update/', views.admin_update, name='admin_update'),
    path('<int:user_pk>/delete/', views.delete, name='delete'),
]