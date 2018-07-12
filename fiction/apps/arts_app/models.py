from django.db import models
from django.utils import timezone
# Create your models here.
from fiction.settings import SEX_CHOICES,FLAGS_CHOICES,DINNER_CHOICES,PAY_CHOICES


class ArtsUser(models.Model):
    username = models.CharField(max_length=50, verbose_name='用户名')
    password = models.CharField(max_length=100, verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱')
    createtime = models.DateTimeField(default=timezone.now, db_index=True,
                                      verbose_name='添加时间')
    flag = models.IntegerField(default=0, verbose_name='控制字段', choices=FLAGS_CHOICES)
    usersex = models.CharField(max_length=10,default=0, verbose_name='性别', choices=SEX_CHOICES)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '会员信息'
        verbose_name_plural = verbose_name
        db_table = 'arts_user'
        ordering = ['-createtime']



