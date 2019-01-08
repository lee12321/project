from django.db import models
from db.base_model import BaseModel
from django.core.exceptions import ValidationError


class Province(BaseModel):
    name = models.CharField(max_length=32, verbose_name='省名')

    def __str__(self):
        return self.name


class City(BaseModel):
    name = models.CharField(max_length=32, verbose_name='市名')
    province = models.ForeignKey(to=Province)

    def __str__(self):
        return self.name


class CompanyType(BaseModel):
    """企业类型"""
    type = models.CharField(max_length=20,
                            verbose_name='类型名称'
                            )

    class Meta:
        verbose_name = '企业类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type


class Company(BaseModel):
    """企业用户"""

    user_name = models.CharField(verbose_name='用户名',
                                 max_length=16,
                                 unique=True,
                                 )

    password = models.CharField(verbose_name='用户密码',
                                max_length=32
                                )

    """企业信息"""

    # 状态信息
    State_choices = (
        (1, '提交,待审核'),
        (2, '审核通过'),
        (3, '审核拒绝'),
    )

    c_name = models.CharField(verbose_name='企业名称',
                              max_length=16,
                              default='',
                              blank=True
                              )

    credit_code = models.CharField(verbose_name='信用代码',
                                   max_length=64,
                                   default='',
                                   blank=True
                                   )

    legal_name = models.CharField(verbose_name='法人姓名',
                                  max_length=16,
                                  default='',
                                  blank=True
                                  )

    tel = models.CharField(verbose_name='联系电话',
                           max_length=11,
                           default='',
                           blank=True
                           )

    email = models.CharField(verbose_name='邮箱',
                             max_length=32,
                             default='',
                             blank=True
                             )

    site = models.CharField(verbose_name='注册地址',
                            max_length=64,
                            default='',
                            blank=True
                            )

    province = models.ForeignKey(to=Province,
                                 verbose_name='省',
                                 null=True,
                                 blank=True,
                                 )

    city = models.ForeignKey(to=City,
                             verbose_name='市',
                             null=True,
                             blank=True,
                             )

    c_document = models.ImageField(verbose_name='企业证件',
                                   null=True,
                                   blank=True)

    c_status = models.SmallIntegerField(verbose_name='状态',
                                        choices=State_choices,
                                        default=1,
                                        blank=True
                                        )

    c_type = models.ForeignKey(to='CompanyType',
                               verbose_name='企业类型',
                               null=True,
                               blank=True,
                               )

    class Meta:
        verbose_name = '企业信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.c_name

    def clean(self):
        if self.city is None or self.province is None:
            return None
        elif self.city not in self.province.city_set.all():
            raise ValidationError(_('选择的城市不属于选择的省或暂不支持该城市'))
