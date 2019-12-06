from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    path('', post_list, name='post_list'),  # view.py에 선언된 post_list함수를 실행
]