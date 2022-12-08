from django.shortcuts import render
from django.views.generic.base import View
from public.RsaCrypto import RsaCrypto
from django.contrib.auth import authenticate
from apps.login.models import UserProfile

class DisplayView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'display.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'display.html')