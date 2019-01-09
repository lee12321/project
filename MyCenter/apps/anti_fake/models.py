from django.db import models
from db.base_model import BaseModel
from product.models import Product, Category
from company.models import Company

# Create your models here.
# 假冒产品信息
"""
class Counterfeit_prodect(BaseModel):
    cpro_name = models.OneToOneField(to=Product,
                                     related_name='p_name',
                                     verbose_name='产品名称',
                                     )
    cpro_type = models.OneToOneField(to=Product,
                                     related_name='p_type',
                                     verbose_name='产品类型',
                                     )
    cpro_company = models.OneToOneField(to=Product,
                                        related_name='company',
                                        verbose_name='生产厂商',
                                        )
    cpro_standard = models.OneToOneField(to=Product,
                                         related_name='p_standard',
                                         verbose_name='产品规格',
                                         )
    cpro_date = models.OneToOneField(to=Product,
                                     related_name='p_date',
                                     verbose_name='生产日期',
                                     )
    cpro_period = models.OneToOneField(to=Product,
                                       related_name='p_period',
                                       verbose_name='保质期',
                                       )
    cpro_place = models.OneToOneField(to=Product,
                                      related_name='p_place',
                                      verbose_name='产地',
                                      )
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
    logistics = models.IntegerField(verbose_name='物流码')
    category = models.ForeignKey(to=Category,
                                 verbose_name='产品类别'
                                 )
    real_company = models.ForeignKey(to=Company,
                                verbose_name='生产企业',
                                )
    information = models.BooleanField(choices=is_info_choices,
                                      verbose_name='防伪溯源信息',
                                      default=0,
                                      )
    query_time = models.DateField(verbose_name='查询时间')
    query_site = models.CharField(max_length=50,
                                  verbose_name='查询地点',
                                  )
    query_id = models.IntegerField(verbose_name='查询id')
"""
