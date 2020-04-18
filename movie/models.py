from django.db import models
from django.core import validators


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'Genre'


class Movie(models.Model):
    # 电影名
    name = models.CharField(max_length=256)
    # 海报
    poster = models.FileField(max_length=256)
    # 持续时间
    duration = models.CharField(max_length=256)
    # 类型
    genre = models.ManyToManyField(Genre)
    # 发行时间
    release_time = models.CharField(max_length=256)
    # 简介
    intro = models.TextField()
    # 导演
    director = models.CharField(max_length=256)
    # 编剧
    writers = models.CharField(max_length=256)
    # 演员
    actors = models.CharField(max_length=512)

    class Meta:
        db_table = 'Movie'

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
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    # 评分的电影
    mid = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # 分数，范围是0.5~5,步长是0.5，用户不能出现1.3,1.4等评分
    score = models.FloatField(validators=[validators.MinValueValidator(0),validators.MaxLengthValidator(5)])
    # 评论，可选
    comment = models.TextField(blank=True)

    class Meta:
        db_table = 'Movie_rating'






