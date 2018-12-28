from django.contrib import admin
from product.models import Category, Product

admin.site.site_header = "全国产品防伪溯源验证公共平台大数据监管中心"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # 产品分类
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # 产品分类
    pass
