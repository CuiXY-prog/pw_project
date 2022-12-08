"""pw_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from apps.login.views import LoginView, PersonalCenterView
from apps.home.views import HomePageView
from apps.display.views import DisplayView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),                  # 登录机制
    path('', HomePageView.as_view(), name='home'),                      # 主页
    path('pcenter/', PersonalCenterView.as_view(), name='login'),       # 个人中心
    path('display/', DisplayView.as_view(), name='display'),            # 个人中心
]
