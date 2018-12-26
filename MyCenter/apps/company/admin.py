from django.contrib import admin

from company.models import CompanyType,Company_content

admin.site.site_header = '后台企业管理平台'
@admin.register(CompanyType)
class CompanyTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Company_content)
class Company_contentAdmin(admin.ModelAdmin):
    pass
