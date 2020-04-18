from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from django.contrib import messages
from .forms import RegisterForm,LoginForm
from django.http import HttpResponse,request
from .models import User,Movie


# Create your views here.

def index(request):
    # return HttpResponse("ok")
    return render(request, 'movie/index.html')

# 注册视图
class RegisterView(View):
    def get(self,request):
        return render(request,'movie/register.html')

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
        return render(request,'movie/login.html')

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('name')
            pwd=form.cleaned_data.get('password')
            user=User.objects.filter(name=username,password=pwd).first()
            if user:
                request.session['user_id']=user.id
                return redirect(reverse('movie:index'))
            else:
                print('用户名或者密码错误')
                # messages.add_message(request,messages.INFO,'用户名或者密码错误!')
                messages.info(request,'用户名或者密码错误!')
                return redirect(reverse('movie:login'))
        else:
            errors=form.errors.get_json_data()
            for error in errors:
                messages.info(request,error)
            print(form.errors.get_json_data())
            return redirect(reverse('movie:login'))

# def login(request):
#     return render(request,'movie/')