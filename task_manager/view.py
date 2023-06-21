from django.shortcuts import render
from django.views import View


class HomePageViews(View):

    def get(self, request):
        return render(request, 'index.html')


class Login(View):

    def post(self, request):
        pass


class Logout(View):

    def post(self, request):
        pass

