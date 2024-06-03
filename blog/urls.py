from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', BlogList.as_view()), #BlogList 클래스 속에 들어가서 함수까지 자동으로 실행 가능. 함수이름 안 불러줘도 됨.
    path('<int:pk>/', BlogDetail.as_view()), #여기서 pk는 blog_detail함수의 인자 pk를 말함

]

