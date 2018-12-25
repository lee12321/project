from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
# Create your models here.


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    