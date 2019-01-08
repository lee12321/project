from django.db import models
from db.base_model import BaseModel


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
                              )

    credit_code = models.CharField(verbose_name='信用代码',
                                   max_length=64,
                                   )

    legal_name = models.CharField(verbose_name='法人姓名',
                                  max_length=16,
                                  )

    tel = models.CharField(verbose_name='联系电话',
                           max_length=11,
                           )

    email = models.CharField(verbose_name='邮箱',
                             max_length=32,
                             )

    site = models.CharField(verbose_name='注册地址',
                            max_length=64,
                            )
    business_site = models.CharField(verbose_name='工商地址',
                                     max_length=64,

                                     )
    time_limit = models.DateField(verbose_name='营业期限')
    scope = models.CharField(verbose_name='经营范围',
                             max_length=64,

                             )
    province = models.CharField(verbose_name='省',
                                max_length=32,
                                )

    city = models.CharField(verbose_name='市',
                            max_length=32,
                            )

    c_document = models.ImageField(verbose_name='企业证件')

    c_status = models.SmallIntegerField(verbose_name='状态',
                                        choices=State_choices,
                                        )

    c_type = models.ForeignKey(to='CompanyType',
                               verbose_name='企业类型',
                               )

    class Meta:
        verbose_name = '用户信息管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.c_name
