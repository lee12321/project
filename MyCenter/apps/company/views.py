from django.shortcuts import render, HttpResponse, get_object_or_404, Http404
from django.views import View
from company.models import CompanyType, Company
from django.core import serializers


def company_list(request):
    all_company = Company.objects.all()
    data = serializers.serialize('json', all_company)
    return HttpResponse(data, content_type="application/json")


def company_detail(request, c_id):
    company = get_object_or_404(Company, pk=c_id)
    data = serializers.serialize('json', (company,))
    return HttpResponse(data, content_type="application/json")


def company_type(request):
    company_types = CompanyType.objects.all()
    data = serializers.serialize('json', company_types)
    return HttpResponse(data, content_type="application/json")


def company_search(request):
    c_pro = request.GET.get('c_pro', None)
    c_city = request.GET.get('c_city', None)
    c_cate = request.GET.get('c_cate', None)
    companys = Company.objects.all()
    if c_cate:
        companys = companys.filter(c_cate=c_cate)
    if c_city:
        companys = companys.filter(c_city=c_city)
    if c_pro:
        companys = companys.filter(c_pro=c_pro)

    data = serializers.serialize('json', companys)
    return HttpResponse(data, content_type="application/json")
