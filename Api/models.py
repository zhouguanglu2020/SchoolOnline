from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=255, verbose_name="用户名", unique=True, db_index=True)
    password = models.CharField(max_length=255, verbose_name="密码")
    nickname = models.CharField(max_length=255, verbose_name="昵称")
    avatar = models.ImageField(upload_to="User_avatar/%Y/%m/%d/", max_length=255,
                               default="https://static.mukewang.com/static/img/avatar_default.png",
                               verbose_name="头像")
    sex = models.CharField(max_length=5, choices=(('male', '男'), ('female', '女')), default='male', verbose_name="性别")
    job = models.CharField(max_length=255, default="", verbose_name="工作")
    city = models.CharField(max_length=255, default="", verbose_name="城市")
    signature = models.CharField(max_length=255, default="", verbose_name="个性签名")
    hour = models.IntegerField(default=0, verbose_name="学习时长")
    exp = models.IntegerField(default=0, verbose_name="学习经验数")
    integral = models.IntegerField(default=0, verbose_name="积分数")
    follow = models.IntegerField(default=0, verbose_name="关注数")
    fans = models.IntegerField(default=0, verbose_name="粉丝数")
    email = models.CharField(max_length=255, default="", verbose_name="邮箱")
    qq = models.CharField(max_length=255, default="", verbose_name="qq")
    phone = models.CharField(max_length=255, default="", verbose_name="手机号")
    wechat = models.CharField(max_length=255, default="", verbose_name="微信")
    weibo = models.CharField(max_length=255, default="", verbose_name="微博")
    create_time = models.DateTimeField(auto_now=True, verbose_name="注册时间")

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

class Bill(models.Model):
    '''
    订单信息
    '''
    userid = models.CharField(max_length=255, verbose_name="用户id")
    orderno = models.CharField(max_length=255, verbose_name="订单号")
    name = models.CharField(max_length=255, verbose_name="课程名字")
    time = models.CharField(max_length=255, verbose_name="时间")
    cost = models.IntegerField(default=0, verbose_name="消费金额")
    way = models.ForeignKey("RechargePay", on_delete=models.DO_NOTHING, verbose_name="账单支方式", default="", null=True,
                            blank=True, db_constraint=False, )

    class Meta:
        verbose_name = 'Bill'
        verbose_name_plural = verbose_name


class Address(models.Model):
    userid = models.CharField(max_length=255, verbose_name="用户id")
    name = models.CharField(max_length=255, verbose_name="用户名")
    phone = models.CharField(max_length=255, verbose_name="手机号")
    area = models.CharField(max_length=255, verbose_name="地区")
    address = models.CharField(max_length=255, verbose_name="地址")
    postcode = models.CharField(max_length=255, verbose_name="邮编")
    isDefault = models.BooleanField(verbose_name="是否默认", default=False)

    class Meta:
        verbose_name = '地址信息'
        verbose_name_plural = verbose_name