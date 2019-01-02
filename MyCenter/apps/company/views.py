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
    c_prov = request.GET.get('c_prov', None)
    c_city = request.GET.get('c_city', None)
    c_type = request.GET.get('c_type', None)
    company = Company.objects.all()
    if c_type:
        company = company.filter(c_type=c_type)
    if c_city:
        company = company.filter(c_city=c_city)
    if c_prov:
        company = company.filter(c_pro=c_prov)

    data = serializers.serialize('json', company)
    return HttpResponse(data, content_type="application/json")
