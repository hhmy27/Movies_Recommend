from django.urls import path, reverse
from . import views

app_name = 'movie'

urlpatterns = [
    # 默认首页
    # path('', views.index,name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('hot', views.PopularMovieView.as_view(), name='hot'),
    # 登录
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.UserLogout, name='logout'),
    # 注册
    path('register', views.RegisterView.as_view(), name='register'),
    # 分类查看
    path('tag', views.TagView.as_view(), name='tag'),
    # 搜索功能
    path('search', views.SearchView.as_view(), name='search'),
    path('detail/<int:pk>', views.MovieDetailView.as_view(), name='detail'),
    path('history/<int:pk>', views.RatingHistoryView.as_view(),name='history'),
    # 删除记录
    path('del_rec/<int:pk>',views.delete_recode,name='delete_record')
    # path('fixdb',views.fixdb,name='fixdb')
]
