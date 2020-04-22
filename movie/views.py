import csv
import os.path
from django.db.models import Avg,Count
from django.contrib import messages
from .forms import RegisterForm,LoginForm
from django.http import HttpResponse,request
from django.views.generic import View,ListView,DetailView
from .models import User,Movie,Genre,Movie_rating
from django.shortcuts import render,redirect,reverse

# DO NOT MAKE ANY CHANGES
BASE = os.path.dirname(os.path.abspath(__file__))


'''!!! 导入csv文件用'''
# def get_genre():
#     '''导入所有电影类型'''
#     path=os.path.join(BASE,'static\movie\info\genre.txt')
#     with open(path) as fb:
#         for line in fb:
#             Genre.objects.create(name=line.strip())
#
# def get_movie_info():
#     '''导入所有电影信息，设置它们的类型'''
#     path=os.path.join(BASE,'static\movie\info\info.csv')
#     with open(path) as fb:
#         reader=csv.reader(fb)
#         title=reader.__next__()
#         # 读取title信息 id,name,url,time,genre,release_time,intro,directores,writers,starts
#         # 这里的id是imbd的id，根据它来访问static文件夹下面的poster
#         title_dct=dict(zip(title,range(len(title))))
#         # print(title_dct)
#         # print(path)
#         for i,line in enumerate(reader):
#             m=Movie.objects.create(name=line[title_dct['name']],
#                                  movie_id=line[title_dct['id']],
#                                  time=line[title_dct['time']],
#                                  release_time=line[title_dct['release_time']],
#                                  intro=line[title_dct['intro']],
#                                  director=line[title_dct['directors']],
#                                  writers=line[title_dct['writers']],
#                                  actors=line[title_dct['starts']])
#             # 必须要先保存才能建立关系
#             m.save()
#             # 建立类型关系
#             for genre in line[title_dct['genre']].split('|'):
#                 # 找到类型 genre_object
#                 go=Genre.objects.filter(name=genre).first()
#                 # print(go)
#                 m.genre.add(go)
#             if i%1000==0:
#                 print(i)    # 控制台查看进度用
#             # pass
#
# def get_user_rating():
#     '''
#     获取ratings文件，设置用户信息和对电影的评分
#     由于用户没有独立的信息，默认用这种方式保存用户User: name=userId,password=userId,email=userId@1.com
#     通过movie_Id对电影进行关联，设置用户对电影的评分,comment默认为空
#     '''
#     path = os.path.join(BASE, r'static\movie\info\ratings.csv')
#     with open(path) as fb:
#         reader=csv.reader(fb)
#         # userId,movieId,rating,timestamp,timestamp不用管
#         title=reader.__next__()
#         title_dct=dict(zip(title,range(len(title))))
#         # csv文件中，一条记录就是一个用户对一部电影的评分和时间戳，一个用户可能有多条评论
#         # 所以要先取出用户所有的评分，设置成一个字典,格式为{ user:{movie1:rating, movie2:rating, ...}, ...}
#         user_id_dct=dict()
#         for line in reader:
#             user_id=line[title_dct['userId']]
#             movie_id=line[title_dct['movieId']]
#             rating=line[title_dct['rating']]
#             user_id_dct.setdefault(user_id,dict())
#             user_id_dct[user_id][movie_id]=rating
#     # 对所有用户和评分记录
#     for user_id,ratings in user_id_dct.items():
#         u=User.objects.create(name=user_id,password=user_id,email=f'{user_id}@1.com')
#         # 必须先保存
#         u.save()
#         # 开始加入评分记录
#         for movie_id,rating in ratings.items():
#             # Movie_rating(uid=)
#             movie=Movie.objects.get(movie_id=movie_id)
#             relation=Movie_rating(user=u,movie=movie,score=rating,comment='')
#             relation.save()
#             # break
#         print(f'{user_id} process success')
#         # break

# def index(request):
#     # get_genre()
#     # get_movie_info()
#     # get_user_rating()
#     context={'movie':Movie.objects.filter(name="Toy Story (1995) ").first()}
#     # print(Movie.objects.filter(name="Toy Story (1995) ").first())
#     return render(request, 'movie/index.html',context=context)
'''!!! 导入csv文件用'''
# ListView继承类
# 尝试让其它的ListView继承这个类，不过会报错，没有找到合适的继承方式
# class DisplayMovieView(ListView):
#     model = Movie
#     template_name = 'movie/index.html'
#     paginate_by = 15
#     context_object_name = 'movies'
#     ordering = 'movie_id'
#     page_kwarg = 'p'
#
#     def get_queryset(self):
#         # 返回前1000部电影
#         return Movie.objects.filter(movie_id__lte=1000)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(IndexView, self).get_context_data(*kwargs)
#         paginator = context.get('paginator')
#         page_obj = context.get('page_obj')
#         pagination_data = self.get_pagination_data(paginator, page_obj)
#         context.update(pagination_data)
#         print(context)
#         return context
#
#     def get_pagination_data(self, paginator, page_obj, around_count=2):
#         current_page = page_obj.number
#
#         if current_page <= around_count + 2:
#             left_pages = range(1, current_page)
#             left_has_more = False
#         else:
#             left_pages = range(current_page - around_count, current_page)
#             left_has_more = True
#
#         if current_page >= paginator.num_pages - around_count - 1:
#             right_pages = range(current_page + 1, paginator.num_pages + 1)
#             right_has_more = False
#         else:
#             right_pages = range(current_page + 1, current_page + 1 + around_count)
#             right_has_more = True
#         return {
#             'left_pages': left_pages,
#             'right_pages': right_pages,
#             'current_page': current_page,
#             'left_has_more': left_has_more,
#             'right_has_more': right_has_more
#         }


class IndexView(ListView):
    model = Movie
    template_name = 'movie/index.html'
    paginate_by = 15
    context_object_name = 'movies'
    ordering = 'movie_id'
    page_kwarg = 'p'

    def get_queryset(self):
        # 返回前1000部电影
        return Movie.objects.filter(movie_id__lte=1000)

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(IndexView,self).get_context_data(*kwargs)
        paginator=context.get('paginator')
        page_obj=context.get('page_obj')
        pagination_data=self.get_pagination_data(paginator,page_obj)
        context.update(pagination_data)
        print(context)
        return context

    def get_pagination_data(self,paginator,page_obj,around_count=2):
        current_page=page_obj.number

        if current_page<=around_count+2:
            left_pages=range(1,current_page)
            left_has_more=False
        else:
            left_pages = range(current_page-around_count, current_page)
            left_has_more=True

        if current_page>=paginator.num_pages-around_count-1:
            right_pages=range(current_page+1,paginator.num_pages+1)
            right_has_more=False
        else:
            right_pages = range(current_page + 1, current_page+1+around_count)
            right_has_more = True
        return {
            'left_pages':left_pages,
            'right_pages':right_pages,
            'current_page':current_page,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more
        }

class PopularMovieView(ListView):
    model = Movie
    template_name = 'movie/hot.html'
    paginate_by = 15
    context_object_name = 'movies'
    # ordering = 'movie_rating__score'
    page_kwarg = 'p'

    def get_queryset(self):
        # 返回前100部最多人评分的电影
        # 先获取每一部电影自身的平均评分
        # ratings=Movie_rating.objects.aggregate(Avg('score'))
        # movies=Movie.objects.annotate(score=Avg('movie_rating__score')).order_by('-score')[:100]
        movies=Movie.objects.annotate(nums=Count('movie_rating__score')).order_by('-nums')[:100]
        print(movies)
        return movies[:100]

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(PopularMovieView,self).get_context_data(*kwargs)
        paginator=context.get('paginator')
        page_obj=context.get('page_obj')
        pagination_data=self.get_pagination_data(paginator,page_obj)
        context.update(pagination_data)
        # print(context)
        return context

    def get_pagination_data(self,paginator,page_obj,around_count=2):
        current_page=page_obj.number

        if current_page<=around_count+2:
            left_pages=range(1,current_page)
            left_has_more=False
        else:
            left_pages = range(current_page-around_count, current_page)
            left_has_more=True

        if current_page>=paginator.num_pages-around_count-1:
            right_pages=range(current_page+1,paginator.num_pages+1)
            right_has_more=False
        else:
            right_pages = range(current_page + 1, current_page+1+around_count)
            right_has_more = True
        return {
            'left_pages':left_pages,
            'right_pages':right_pages,
            'current_page':current_page,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more
        }

class TagView(ListView):
    model = Movie
    template_name = 'movie/tag.html'
    paginate_by = 15
    context_object_name = 'movies'
    # ordering = 'movie_rating__score'
    page_kwarg = 'p'

    def get_queryset(self):
        if 'genre' not in self.request.GET.dict().keys():
            movies=Movie.objects.all()
            return movies[100:200]
        else:
            movies=Movie.objects.filter(genre__name=self.request.GET.dict()['genre'])
            print(movies)
            return movies[:100]


    def get_context_data(self, *, object_list=None, **kwargs):
        # self.genre=self.request.GET.dict()['genre']
        context=super(TagView,self).get_context_data(*kwargs)
        paginator=context.get('paginator')
        page_obj=context.get('page_obj')
        pagination_data=self.get_pagination_data(paginator,page_obj)
        context.update(pagination_data)
        return context

    def get_pagination_data(self,paginator,page_obj,around_count=2):
        current_page=page_obj.number

        if current_page<=around_count+2:
            left_pages=range(1,current_page)
            left_has_more=False
        else:
            left_pages = range(current_page-around_count, current_page)
            left_has_more=True

        if current_page>=paginator.num_pages-around_count-1:
            right_pages=range(current_page+1,paginator.num_pages+1)
            right_has_more=False
        else:
            right_pages = range(current_page + 1, current_page+1+around_count)
            right_has_more = True
        return {
            'left_pages':left_pages,
            'right_pages':right_pages,
            'current_page':current_page,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more
        }

class SearchView(ListView):
    model = Movie
    template_name = 'movie/search.html'
    paginate_by = 15
    context_object_name = 'movies'
    # ordering = 'movie_rating__score'
    page_kwarg = 'p'

    def get_queryset(self):
        movies=Movie.objects.filter(name__icontains=self.request.GET.dict()['keyword'])
        print(movies)
        return movies


    def get_context_data(self, *, object_list=None, **kwargs):
        # self.genre=self.request.GET.dict()['genre']
        context=super(SearchView,self).get_context_data(*kwargs)
        paginator=context.get('paginator')
        page_obj=context.get('page_obj')
        pagination_data=self.get_pagination_data(paginator,page_obj)
        context.update(pagination_data)
        context.update({'keyword':self.request.GET.dict()['keyword']})
        return context

    def get_pagination_data(self,paginator,page_obj,around_count=2):
        current_page=page_obj.number

        if current_page<=around_count+2:
            left_pages=range(1,current_page)
            left_has_more=False
        else:
            left_pages = range(current_page-around_count, current_page)
            left_has_more=True

        if current_page>=paginator.num_pages-around_count-1:
            right_pages=range(current_page+1,paginator.num_pages+1)
            right_has_more=False
        else:
            right_pages = range(current_page + 1, current_page+1+around_count)
            right_has_more = True
        return {
            'left_pages':left_pages,
            'right_pages':right_pages,
            'current_page':current_page,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more
        }



# 注册视图
class RegisterView(View):
    def get(self,request):
        return render(request, 'movie/register.html')

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            # 没毛病，保存
            form.save()
            return redirect(reverse('movie:index'))
        else:
            # 表单验证失败，重定向到注册页面
            errors=form.get_errors()
            for error in errors:
                messages.info(request,error)
            print(form.errors.get_json_data())
            return redirect(reverse('movie:register'))


# 登录视图
class LoginView(View):
    def get(self,request):
        return render(request, 'movie/login.html')

    def post(self,request):
        print(request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('name')
            print(username)
            pwd=form.cleaned_data.get('password')
            user=User.objects.filter(name=username,password=pwd).first()
            if user:
                # 登录成功，在session 里面加上当前用户的id，作为标识
                request.session['user_id']=user.id
                return redirect(reverse('movie:index'))
            else:
                print('用户名或者密码错误')
                # messages.add_message(request,messages.INFO,'用户名或者密码错误!')
                messages.info(request,'用户名或者密码错误!')
                return redirect(reverse('movie:login'))
        else:
            print("error!!!!!!!!!!!")
            errors=form.get_errors()
            for error in errors:
                messages.info(request,error)
            print(form.errors.get_json_data())
            return redirect(reverse('movie:login'))


class MovieDetailView(DetailView):
    '''用户详情页面'''
    model=Movie
    template_name = 'movie/detail.html'
    context_object_name = 'movie'

