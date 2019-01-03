from django.contrib import admin

from .models import CompanyType, Company

# admin.site.site_header = '后台企业管理平台'


@admin.register(CompanyType)
class CompanyTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
