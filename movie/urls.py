from django.urls import path, reverse
from . import views

app_name = 'movie'

urlpatterns = [
    # 默认首页
    path('', views.index,name='index'),
    # 登录
    path('login',views.LoginView.as_view(),name='login'),
    # 注册
    path('register',views.RegisterView.as_view(),name='register')
    # path('/logout',views)
]
