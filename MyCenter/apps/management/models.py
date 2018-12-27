from django.db import models
from django.contrib.auth.models import Group as _Group, PermissionsMixin
from django.contrib.auth.models import (AbstractUser, BaseUserManager)


# Create your models here.

class User(AbstractUser):
    class Meta:
        verbose_name = '管理员'
        verbose_name_plural = '管理员'

    can_edit_product = models.BooleanField(default=False, verbose_name='可编辑产品')
    can_edit_company = models.BooleanField(default=False, verbose_name='可编辑公司')

    def __str__(self):
        return self.username
