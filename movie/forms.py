from django import forms
# from django.forms  import ModelForm
from movie.models import User

class RegisterForm(forms.ModelForm):
    '''注册用的表单'''
    password_repeat=forms.CharField(max_length=256)
    def get_errors(self):
        errors=self.errors.get_json_data()
        errors_lst=[]
        for messages in errors.values():
            for message_dict in messages:
                for key,message in message_dict.items():
                    if key=='message':
                        errors_lst.append(message)
        return errors_lst

    # 普通验证之后的最后一层验证
    # 验证密码
    def clean(self):
        cleaned_data=super(RegisterForm,self).clean()
        pwd=cleaned_data.get('password')
        password_repeat=cleaned_data.get('password_repeat')
        if pwd != password_repeat:
            raise forms.ValidationError(message='两次密码输入不一致！')
        return cleaned_data

    class Meta:
        model = User
        fields=['name','password','email']

class LoginForm(forms.Form):
    '''
    用于登录的表单
    登录的表单不要使用ModelForm，因为这会在数据库中验证，会出现类似User with this Name already exists的错误
    '''
    name=forms.CharField(max_length=128)
    password=forms.CharField(max_length=256)

    def get_errors(self):
        errors=self.errors.get_json_data()
        errors_lst=[]
        for messages in errors.values():
            for message_dict in messages:
                for key,message in message_dict.items():
                    if key=='message':
                        errors_lst.append(message)
        return errors_lst