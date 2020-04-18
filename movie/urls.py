from django.urls import path, reverse
from . import views

# app_name = 'movie'

urlpatterns = [
    # 默认首页
    path('', views.index,name='index'),
    # 登录
    path('/login',views.login,name='login'),
    # 注册
    path('/register',views.register,name='register')
    # path('/logout',views)
]
