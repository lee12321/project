from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class CategoryView(View):
    def get(self, request, cate_id=0):
        return HttpResponse('666')

    def post(self, request):
        pass
