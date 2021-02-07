from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:question_text>/', views.detail, name='detail'),
    path('user/signup', views.userSignup, name='userSignup'),
    path('user/login', views.userLogin, name='userLogin'),
    path('user/docLogin', views.docLogin, name='docLogin'),
    path('user/docSignup', views.docSignup, name='docSignup'),
]