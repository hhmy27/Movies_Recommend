from django import forms
# from django.forms  import ModelForm
from movie.models import User, Movie_rating


class RegisterForm(forms.ModelForm):
    '''注册用的表单'''
    password_repeat = forms.CharField(max_length=256)

    def get_errors(self):
        errors = self.errors.get_json_data()
        errors_lst = []
        for messages in errors.values():
            for message_dict in messages:
                for key, message in message_dict.items():
                    if key == 'message':
                        errors_lst.append(message)
        return errors_lst

    # 普通验证之后的最后一层验证
    # 验证密码
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        pwd = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')
        if pwd != password_repeat:
            raise forms.ValidationError(message='两次密码输入不一致！')
        return cleaned_data

    class Meta:
        model = User
        fields = ['name', 'password', 'email']


class LoginForm(forms.ModelForm):
    '''
    用于登录的表单
    '''
    name = forms.CharField(max_length=128)
    remember = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ['password']

    def get_errors(self):
        errors = self.errors.get_json_data()
        errors_lst = []
        for messages in errors.values():
            for message_dict in messages:
                for key, message in message_dict.items():
                    if key == 'message':
                        errors_lst.append(message)
        return errors_lst


class CommentForm(forms.ModelForm):
    # 表单验证通过后再验证分数是否为0
    def clean(self):
        cleaned_data = super(CommentForm, self).clean()
        score = cleaned_data.get('score')
        if score == 0:
            raise forms.ValidationError(message='评分不能为空！')
        else:
            return cleaned_data

    class Meta:
        # 电影评分，只记录评分和评论
        model = Movie_rating
        fields = ['score', 'comment']
