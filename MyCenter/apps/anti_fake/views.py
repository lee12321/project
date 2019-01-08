from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from anti_fake.models import Counterfeit_prodect
from anti_fake.serializers import CounterfeitSerializer
from django.http import JsonResponse


# Create your views here.
"""
@csrf_exempt
def sdypro(request):
    if request.method == 'GET':
        products = Counterfeit_prodect.objects.all()
        serializer = CounterfeitSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
"""