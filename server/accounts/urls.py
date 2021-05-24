  
from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('profile/',views.profile),
    path('login/kakao/', views.kakao_login, name='kakao_login'),
    path('login/kakao/callback/',views.kakao_callback, name='kakao_callback'),   

]