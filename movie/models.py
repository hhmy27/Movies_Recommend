from django.db import models
from django.db.models import Avg
from django.core import validators


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'Genre'
    def __str__(self):
        return f"<Genre:{self.name}>"

class Movie(models.Model):
    # 电影名
    name = models.CharField(max_length=256)
    # movie_id，用来对应static里面的海报，为了方便，这个并没有设置成主键，而是使用django默认的自增id作为主键
    # 但是大部分查询仍然使用movie_id来做查询
    movie_id = models.IntegerField()
    # 时长
    time = models.CharField(max_length=256,blank=True)
    # 类型
    genre = models.ManyToManyField(Genre)
    # 发行时间
    release_time = models.CharField(max_length=256,blank=True)
    # 简介
    intro = models.TextField(blank=True)
    # 导演
    director = models.CharField(max_length=256,blank=True)
    # 编剧
    writers = models.CharField(max_length=256,blank=True)
    # 演员
    actors = models.CharField(max_length=512,blank=True)

    class Meta:
        db_table = 'Movie'

    def __str__(self):
        return f"<Movie:{self.name},{self.movie_id}>"

    def get_score(self):
        # 定义一个获取平均分的方法，模板中直接调用即可
        # 格式 {'score__avg': 3.125}
        result_dct=self.movie_rating_set.aggregate(Avg('score'))
        try:
            # 只保留一位小数
            result=round(result_dct['score__avg'],1)
        except TypeError:
            return 0
        else:
            return result

    def get_user_score(self,user):
        return self.movie_rating_set.filter(user=user).values('score')

    def get_score_int_range(self):
        return range(int(self.get_score()))

    def get_genre(self):
        genre_dct=self.genre.all().values('name')
        genre_lst=[]
        for dct in genre_dct.values():
            genre_lst.append(dct['name'])
        return genre_lst

class User(models.Model):
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    rating_movies = models.ManyToManyField(Movie, through="Movie_rating")

    def __str__(self):
        return "<USER:( name: {:},password: {:},email: {:} )>".format(self.name, self.password, self.email)

    class Meta:
        db_table = 'User'


class Movie_rating(models.Model):
    # 评分的用户
    user = models.ForeignKey(User, on_delete=models.CASCADE,unique=False)
    # 评分的电影
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,unique=False)
    # 分数
    score = models.FloatField()
    # 评论，可选
    comment = models.TextField(blank=True)

    class Meta:
        db_table = 'Movie_rating'






