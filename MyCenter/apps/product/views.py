from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.core import serializers
from django.http import JsonResponse
from product.models import Category, Product
import json

"""
class CategoryView(View):
    def get(self, request, cate_id=0):
        cate_id = int(cate_id)
        # 查询所有分类
        categorys = Category.objects.filter(is_delete=False)
        # 查询出所有的产品
        # goods = Product.objects.filter(is_delete=False)

        # 根据传入id查找对应分类
        category = Category.objects.get(pk=cate_id)
        # 获取对应分类下的商品
        goods = category.product_set.all()

        context = {
            'categorys': categorys,
            'goods': goods,
        }
        return render(request, 'product/product.html', context)

    def post(self, request):
        pass
"""


# 对应分类下的商品
class CategoryView(View):
    def get(self, request, cate_id=0):
        # cate_id = request.GET.get('cate_id')
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
        goods_data = serializers.serialize('json', goods)
        goods_data = json.loads(goods_data)
        list = []
        for good in goods_data:
            good['error'] = 0
            list.append(good)
        goods_data = json.dumps(list)
        print(goods_data)
        # return JsonResponse(goods_data)
        return HttpResponse(goods_data, content_type='application/json')

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
class cate_searchVie(View):
    def get(self, request):
        pro_province = request.GET.get('pro_province', None)
        pro_city = request.GET.get('pro_city', None)
        pro_product = request.GET.get('pro_product', None)
        products = Product.objects.all()
        if pro_province:
            products = products.filter()

    def post(self, request):
        pass
