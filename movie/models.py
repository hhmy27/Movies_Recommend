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
    # movie_id，用来对应static里面的海报
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
        # 只保留一位小数
        result=round(result_dct['score__avg'],1)
        # print(result)
        return result

class User(models.Model):
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    rating_movies = models.ManyToManyField(Movie, through="Movie_rating")

    def __str__(self):
        return "<USER:( name: {:},password: {:},email: {:})>".format(self.name, self.password, self.email)

    class Meta:
        db_table = 'User'


class Movie_rating(models.Model):
    # 评分的用户
    user = models.ForeignKey(User, on_delete=models.CASCADE,unique=False)
    # 评分的电影
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,unique=False)
    # 分数，范围是0.5~5,步长是0.5，用户不能出现1.3,1.4等评分
    score = models.FloatField(validators=[validators.MinValueValidator(0),validators.MaxLengthValidator(5)])
    # 评论，可选
    comment = models.TextField(blank=True)

    class Meta:
        db_table = 'Movie_rating'






