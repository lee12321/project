from django.db import models
from django.contrib.auth.models import (AbstractUser, BaseUserManager)


# Create your models here.

class User(AbstractUser):
    class Meta:
        verbose_name = '管理员'
        verbose_name_plural = '管理员'

    def __str__(self):
        return self.username
