from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=30, verbose_name="真实姓名")
    school = models.CharField(max_length=100, verbose_name="学校", blank=True, null=True, default="")
    department = models.CharField(max_length=50, verbose_name="所属院系", blank=True, null=True, default="")
    mobile = models.CharField(max_length=11, null=False, blank=True, verbose_name="联系电话", default="")
    memo = models.TextField('备注', blank=True, null=True, default=None)
    photo = models.ImageField('个人头像', blank=True, help_text="为了节省存储资源，图片采取了字节流的方式保存在数据库中,在这里上传无法生效")

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
