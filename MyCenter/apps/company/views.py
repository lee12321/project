from django.shortcuts import render, HttpResponse, get_object_or_404
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