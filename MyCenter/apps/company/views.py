from django.shortcuts import render, HttpResponse, get_object_or_404, Http404, redirect
from django.views import View
from company.models import CompanyType, Company, Province, City
from product.models import Category
from django.core import serializers
from company.forms import RegisterForm


def company_detail(request, c_id):
    company = get_object_or_404(Company, pk=c_id)
    company_types = CompanyType.objects.all()
    product_types = Category.objects.all()
    context = {'company': company,
               'company_types': company_types,
               'product_types': product_types}
    return render(request, 'company_detail.html', context=context)


def company_type(request):
    pass


def company_search(request):
    c_prov = request.GET.get('c_prov', None)
    c_city = request.GET.get('c_city', None)
    c_type = request.GET.get('c_type', None)
    company = Company.objects.all()
    company_types = CompanyType.objects.all()
    product_types = Category.objects.all()
    if c_type:
        company = company.filter(c_type=c_type)
    if c_city:
        company = company.filter(c_city=c_city)
    if c_prov:
        company = company.filter(c_pro=c_prov)
    company = company.filter(c_status=2)
    context = {'company': company,
               'company_types': company_types,
               'product_types': product_types}

    return render(request, 'company.html', context=context)


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company:search')
        else:
            return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        company = Company.objects.filter(user_name=request.POST.get('user_name', '')).first()
        if company and company.password == request.POST.get('password', ''):
            request.session['user'] = company.pk
            return redirect('company:search')
        else:
            return redirect('company:login')
