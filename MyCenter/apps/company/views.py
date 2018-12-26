from django.shortcuts import render
from django.views import View
from company.models import CompanyType,Company_content

class LoginView(View):
    def get(self,request):
        pass

    def post(self,request):
        pass

class IndexView(View):
    def get(self,request):
        Company_content.objects.filter()



    def post(self,request):
        pass