from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from apps.product.models import Product, Category
from apps.company.models import Company
from django.shortcuts import get_object_or_404
from django.core import serializers


def product_search(request):
    c_prov = request.GET.get('c_prov', None)
    c_city = request.GET.get('c_city', None)
    c_name = request.GET.get('c_name', None)
    p_name = request.GET.get('p_name', None)
    if p_name:
        products = Product.objects.filter(p_name=p_name)
        data = serializers.serialize('json', products)
        return HttpResponse(data, content_type="application/json")
    elif c_prov:
        company = Company.objects.filter(province=c_prov)
        if c_city:
            company = company.filter(city=c_city)
        if c_name:
            company = company.filter(p_name=p_name)
        products = company.product_set.all()
        data = serializers.serialize('json', products)
        return HttpResponse(data, content_type="application/json")
    else:
        products = Product.objects.all()
        data = serializers.serialize('json', products)
        return HttpResponse(data, content_type="application/json")
