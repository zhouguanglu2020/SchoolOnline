from django.db import models

# Create your models here.

class User(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    wechat = models.CharField(max_length=32)
    qq = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
