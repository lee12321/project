from django.db import models
from db.base_model import BaseModel
from product.models import Product, Category
from company.models import Company


# Create your models here.
# 假冒产品信息
class Counterfeit_prodect(BaseModel):
    c_pro = models.ForeignKey(to=Product,
                              verbose_name='假冒产品',
                              )
    number = models.IntegerField(verbose_name='防伪数量')
    epoch = models.DateField(verbose_name='假冒出现时间')
    site = models.CharField(max_length=50,
                            verbose_name='出现地点',
                            )

    class Meta:
        # 定义在后台显示的名称
        verbose_name = "防伪监管"
        # 定义复数时的名称(去掉s)
        verbose_name_plural = verbose_name


# 实时数据
class Realtime(BaseModel):
    is_info_choices = (
        (0, '真'),
        (1, '假'),
    )
    logistics = models.CharField(verbose_name='物流码',
                                 max_length=20,
                                 )
    r_product = models.ForeignKey(to=Product,
                                  verbose_name='产品名称',
                                  default='',
                                  )
    information = models.BooleanField(choices=is_info_choices,
                                      verbose_name='防伪溯源信息',
                                      default=0,
                                      )
    query_type = models.CharField(verbose_name='查询类型',
                                  max_length=20,
                                  )
    query_time = models.DateField(verbose_name='查询时间')
    query_site = models.CharField(max_length=50,
                                  verbose_name='查询地点',
                                  )
    query_id = models.CharField(verbose_name='查询id',
                                max_length=20,
                                )

    class Meta:
        # 定义在后台显示的名称
        verbose_name = "实时数据"
        # 定义复数时的名称(去掉s)
        verbose_name_plural = verbose_name
