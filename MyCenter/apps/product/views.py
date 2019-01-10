from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.core import serializers
from django.http import JsonResponse
from product.models import Category, Product
from company.models import Company, CompanyType
import json


class DetailView(View):
    def get(self, request, pro_id=0):
        pro_id = int(pro_id)
        good_info = Product.objects.get(pk=pro_id)
        company_types = CompanyType.objects.all()
        product_types = Category.objects.all()
        # print(good_info)
        context = {
            'good_info': good_info,
            'company_types': company_types,
            'product_types': product_types
        }
        return render(request, 'details.html', context)

    def post(self, request):
        pass


# 对应分类下的商品
class CategoryView(View):
    def get(self, request):
        company_types = CompanyType.objects.all()
        product_types = Category.objects.all()
        cate_id = request.GET.get('p_type')
        if not cate_id:
            return JsonResponse({'error': 2, 'msg': '参数不存在!'})
        try:
            cate_id = int(cate_id)
        except:
            return JsonResponse({'error': 3, 'msg': '参数错误!'})
        # 根据传来的cate_id找到对应分类
        category = Category.objects.get(pk=cate_id)
        # 获取对应产品
        goods = category.product_set.all()
        # goods_data = serializers.serialize('json', goods)
        # goods_data = json.loads(goods_data)
        # list = []
        # for good in goods_data:
        #     good['error'] = 0
        #     list.append(good)
        # goods_data = json.dumps(list)
        # print(goods_data)
        # return JsonResponse({'data': goods, 'error': 0})
        # return HttpResponse(goods_data, content_type='application/json')
        return render(request, 'product.html', {'products': goods,
                                                'company_types': company_types,
                                                'product_types': product_types
                                                })

    def post(self, requtst):
        pass


# 产品分类
class cate_proView(View):
    def get(self, requesrt):
        cates = Category.objects.all()
        cates = serializers.serialize('json', cates)
        return HttpResponse(cates, content_type='application/json')

    def post(self, request):
        pass


# 搜索
class CateSearchView(View):
    def get(self, request):
        c_prov = request.GET.get('c_prov', None)
        c_city = request.GET.get('c_city', None)
        c_name = request.GET.get('c_name', None)
        p_name = request.GET.get('p_name', None)
        company_types = CompanyType.objects.all()
        product_types = Category.objects.all()
        if p_name:
            products = Product.objects.filter(p_name=p_name)
            return render(request, 'product.html', {'products': products,
                                                    'company_types': company_types,
                                                    'product_types': product_types})
        elif c_prov:
            company = Company.objects.filter(province=c_prov)
            if c_city:
                company = company.filter(city=c_city)
            if c_name:
                company = company.filter(p_name=c_name)
            products = company.product_set.all()
            return render(request, 'product.html', {'products': products,
                                                    'company_types': company_types,
                                                    'product_types': product_types})
        else:
            products = Product.objects.all()
            return render(request, 'product.html', {'products': products,
                                                    'company_types': company_types,
                                                    'product_types': product_types})

    def post(self, request):
        pass
