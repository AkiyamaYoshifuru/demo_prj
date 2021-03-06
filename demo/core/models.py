from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# 基础用户类型，继承自Django抽象用户型，此类用法是推荐的实践
class User(AbstractUser):
    
    is_officer = models.BooleanField(default=False)
    is_operator = models.BooleanField(default=False)
    
class Officer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    def export_xls():
        pass
    
    def export_pdf():
        pass
    
    def __str__(self):
        return self.user.username
    
    
class Operator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.user.username