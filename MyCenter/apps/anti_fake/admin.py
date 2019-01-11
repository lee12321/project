from django.contrib import admin
from anti_fake.models import Counterfeit_prodect, Realtime


# Register your models here.
@admin.register(Counterfeit_prodect)
class CategoryAdmin(admin.ModelAdmin):
    # 假冒产品
    pass


@admin.register(Realtime)
class CategoryAdmin(admin.ModelAdmin):
    # 实时数据
    pass
