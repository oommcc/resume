from django.contrib.auth.models import AbstractUser
from django.db import models
from resume.utils.models import BaseModel
# Create your models here.



# 用户模型类
class User(AbstractUser):
    '''
    用户表和职位表是多对多
    用户表和简历表   id关联

    '''
    username = models.CharField(unique=True,verbose_name='用户名')
    mobile = models.CharField(max_length=11, unique=True)
    email_active = models.BooleanField(default=False,validators='邮箱验证状态')
    resume = models.CharField(verbose_name='简历')
    user_position = models.CharField(verbose_name='求职职位')


    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

#   用户动态表
class Dynamic(BaseModel):
    '''
    动态表：

    '''
    LIKE_CHOICE = (
        (0,'未点赞'),
        (1,'已点赞'),


    )

    userid = models.ForeignKey(User,on_delete=models.CASCADE(), verbose_name="用户id")
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="用户名")
    dynamic = models.CharField(verbose_name='动态')
    comment = models.CharField(default="",verbose_name='评论')
    is_like = models.SmallIntegerField(choices=LIKE_CHOICE,verbose_name='点赞')
    data_created = models.DateTimeField(verbose_name='发布时间')
    # order = models.IntegerField(verbose_name='顺序')
    # 动态中的图片，最多九张，9个字段
    photo = models.CharField(verbose_name='图片')


class Meta:
    db_table = 'dynamic'
    verbose_name = '用户动态表'
    verbose_name_plural = verbose_name


def __str__(self):
    return self.dynamic

# 用户评论表
class Comment(BaseModel):
    '''
    动态表：

    '''
    LIKE_CHOICE = (
        (0, '未点赞'),
        (1, '已点赞'),

    )

    userid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户id")
    dynamic = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户动态")
    comment = models.CharField(default="", verbose_name='评论')
    is_like = models.SmallIntegerField(choices=LIKE_CHOICE, verbose_name='点赞')
    # data_created = models.DateTimeField(verbose_name='发布时间')
    order = models.IntegerField(verbose_name='顺序')

    class Meta:
        db_table = 'comment'
        verbose_name = '评论表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comment




