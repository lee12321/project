from django.db import models
from db.base_model import BaseModel
from company.models import Company


class Category(BaseModel):
    """产品分类"""
    cate_name = models.CharField(max_length=20,
                                 verbose_name="类型名称",
                                 )

    def __str__(self):
        return self.cate_name

    class Meta:
        # 定义在后台显示的名称
        verbose_name = "产品分类"
        # 定义复数时的名称(去掉s)
        verbose_name_plural = verbose_name


class Product(BaseModel):
    """产品详情"""
    is_status_choices = (
        (0, "初始化"),
        (1, "提交申请"),
        (2, "生产防伪码")
    )
    p_name = models.CharField(verbose_name="产品名称",
                              max_length=50
                              )
    p_type = models.CharField(verbose_name="产品类型",
                              max_length=20
                              )
    company = models.ForeignKey(to=Company,
                                verbose_name="生产厂商",
                                )
    p_standard = models.CharField(verbose_name="产品规格",
                                  max_length=20
                                  )
    p_date = models.DateField(verbose_name="生产日期")
    p_period = models.CharField(verbose_name="保质期",
                                max_length=20
                                )
    p_place = models.CharField(verbose_name="产地",
                               max_length=20
                               )
    p_number = models.CharField(verbose_name='产品编号',
                                max_length=15,
                                )
    anti_fake_logo = models.CharField(verbose_name="防伪标识",
                                      max_length=20,
                                      default="logo",
                                      )
    category_name = models.ForeignKey(to="Category",
                                      verbose_name="分类"
                                      )
    p_status = models.BooleanField(verbose_name="状态",
                                   choices=is_status_choices,
                                   default=0
                                   )
    p_feature = models.CharField(verbose_name="特色",
                                 # 允许表单验证为空
                                 blank=True,
                                 # 允许数据库为空
                                 null=True,
                                 max_length=250
                                 )
    p_operate = models.CharField(verbose_name="生产工艺",
                                 blank=True,
                                 null=True,
                                 max_length=250
                                 )

    def __str__(self):
        return self.p_name

    class Meta:
        # 定义在后台显示的名称
        verbose_name = "产品详情"
        # 定义复数时的名称(去掉s)
        verbose_name_plural = verbose_name
