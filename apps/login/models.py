from django.db import models
from django.contrib.auth.models import AbstractUser
import django.utils.timezone as timezone

class UserProfile(AbstractUser):
    """用户基本信息

    Args:
        AbstractUser (_type_): _description_

    Returns:
        _type_: _description_
    """
    nick_name = models.CharField(max_length=50, verbose_name="昵称", null=True, blank=True)
    user_addtime = models.DateTimeField(verbose_name="记录添加日期", default=timezone.now)
    user_number = models.CharField(max_length=10, verbose_name="员工编号", default="")
    user_department = models.CharField(max_length=50, verbose_name="所在部门", default="")
    user_role = models.CharField(max_length=50, verbose_name="担任角色", default="")
    user_phone = models.CharField(max_length=20, verbose_name="手机号码", default="")
    user_avator = models.ImageField(upload_to='static/imgs/', verbose_name="用户头像")
    
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # 重载对象的描述符
    def __str__(self):
        return self.nick_name

class UserLoginInfo(models.Model):
    """用户登录信息

    Args:
        models (_type_): _description_
    """
    user_id = models.IntegerField(verbose_name="用户ID")
    login_time = models.DateTimeField(verbose_name="登录时间", default=timezone.now)
    login_ip = models.CharField(max_length=10, verbose_name="登录IP", default="")
    equirement_type = models.CharField(max_length=200, verbose_name="设备类型", default="")

    class Meta:
        ordering = ['-login_time']
        verbose_name = "登录信息"
    
    def __str__(self) -> str:
        return str(self.user_id)


class UserOperation(models.Model):
    """用户操作信息

    Args:
        models (_type_): _description_
    """
    user_id = models.IntegerField(verbose_name="用户ID")
    expiration = models.DateTimeField(verbose_name="操作时间", default=timezone.now)
    types = (
        ('0', '查询'),
        ('1', '修改'),
        ('2', '导入')
    )
    type = models.CharField(max_length=1, choices=types)

    class Meta:
        ordering = ['-expiration']
        verbose_name = "操作信息"
        verbose_name_plural = verbose_name

        def __str__(self) -> str:
            return self.expiration.strftime("%Y-%m-%d")
