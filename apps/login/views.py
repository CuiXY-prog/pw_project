from django.shortcuts import render
from django.views.generic.base import View
import time

class LoginView(View):
    """负责登录操作

    Args:
        request (_type_): _description_

    Returns:
        对象: 返回一个网页
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {'isSuccess':'true'})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print(username, password)
        return render(request, 'login.html', {'isSuccess':'false'})