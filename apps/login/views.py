from django.shortcuts import render
from django.views.generic.base import View
from public.RsaCrypto import RsaCrypto
from django.contrib.auth import authenticate
from apps.login.models import UserProfile

class LoginView(View):
    """负责登录操作

    Args:
        request (_type_): _description_

    Returns:
        对象: 返回一个网页
    """
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.rsa = RsaCrypto()
        
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {'isSuccess':'true'})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        darkmode = request.POST.get('darkmode', '')
        if username == '' or password == '' or (darkmode != '' and darkmode != 'yes'):
            return render(request, 'login.html', {'isSuccess':'false'})

        # 验证用户名和密码
        password = self.rsa.decryptData(password)

        if darkmode != '':
            # 如果是工号登录就查询用户名
            user = UserProfile.objects.filter(user_number=username)
            if not user: 
                return render(request, 'login.html', {'isSuccess':'false'})
            username = user[0].username

        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, 'login.html', {'isSuccess':'false'})
        
        return render(request, 'login.html', {'isSuccess':'true'})