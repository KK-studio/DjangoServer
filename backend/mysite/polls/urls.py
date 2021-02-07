from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:question_text>/', views.detail, name='detail'),
    path('user/signup', views.userLogin, name='userLogin'),
]