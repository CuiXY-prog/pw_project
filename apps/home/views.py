from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'home.html')
