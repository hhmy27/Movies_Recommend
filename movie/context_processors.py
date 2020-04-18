from .models import User

# 上下文处理器
def movie_user(request):
    user_id=request.session.get('user_id')
    context={}
    if user_id:
        try:
            user=User.objects.get(pk=user_id)
            context['movie_user']=user
        except:
            pass
    return context
