from django.shortcuts import render
from django.views import View
from anti_fake.models import Counterfeit_prodect, Realtime


# Create your views here.
class SdyproView(View):
    def get(self, request):
        pros = Counterfeit_prodect.objects.all()
        context = {
            'pros': pros,
        }
        return render(request, 'sdypro.html', context)

    def post(self, request):
        pass


class RealView(View):
    def get(self, request):
        data = Realtime.objects.all()
        context = {
            'data': data,
        }
        return render(request, 'reltmdtshow.html', context)

    def post(self, request):
        pass


class RealLookView(View):
    def get(self, request):
        data = Realtime.objects.all()
        context = {
            'data': data,
        }
        return render(request, 'reltmdtshow-look.html', context)

    def post(self, request):
        pass


class LookView(View):
    def get(self, request, pro_id=0):
        data = Realtime.objects.get(logistics=pro_id)
        context = {
            'data': data,
        }
        return render(request, 'look.html', context)

    def post(self, request):
        pass
