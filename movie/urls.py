from django.urls import path, reverse
from . import views

app_name = 'movie'

urlpatterns = [
    # 默认首页
    path('', views.IndexView.as_view(), name='index'),
    # 热门电影
    path('hot', views.PopularMovieView.as_view(), name='hot'),
    # 登录
    path('login', views.LoginView.as_view(), name='login'),
    # 退出
    path('logout', views.UserLogout, name='logout'),
    # 注册
    path('register', views.RegisterView.as_view(), name='register'),
    # 分类查看
    path('tag', views.TagView.as_view(), name='tag'),
    # 搜索功能
    path('search', views.SearchView.as_view(), name='search'),
    # 电影详情页面
    path('detail/<int:pk>', views.MovieDetailView.as_view(), name='detail'),
    # 评分历史页面
    path('history/<int:pk>', views.RatingHistoryView.as_view(),name='history'),
    # 删除记录
    path('del_rec/<int:pk>',views.delete_recode,name='delete_record'),
    # 推荐页面
    path('recommend',views.RecommendMovieView.as_view(),name='recommend'),
    # 导入物品之间的相似度
    # path('calc_movie_similarity',views.calc_movie_similarity,name='calc_similarity')

]
