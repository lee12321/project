from django.shortcuts import render
from django.views import View
from .models import CompanyType, CompanyContent


class ContentView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
