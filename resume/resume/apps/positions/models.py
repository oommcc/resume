from django.db import models

# Create your models here.
# 定义职位模型类数据
from resume.utils.models import BaseModel


class PositionInfo(BaseModel):
    """
    职位数据：

    关系：
    公司表与职位表是：一对多
    简历表与职位表之间 ：一张中间表 职位id与简历id
    用户表和职位表是多对多

    """
    EDUCATION_CHOICES = (
                            (0, '博士后'),
                            (1, '博士'),
                            (2, '硕士'),
                            (3, '本科'),
                            (4, '大专'),
                            (5, '中专'),
                            (6, '高中'),
                            (7, '初中'),
                            (8, '其它'),
                        ),
    EXPERIENCE_CHOICES = (
                             (0, '无经验'),
                             (1, '1年以下'),
                             (2, '1-3年'),
                             (3, '3-5年'),
                             (4, '5-10年'),
                             (5, '10年以上'),
                         ),
    GENDER_CHOICES = (
                         (0, 'male'),
                         (1, 'female')
                     ),
    MERRY_CHOICES = (
        (0, '未婚未孕'),
        (1, '未婚先孕'),
        (2, '已婚未孕'),
        (3, '已婚已孕'),
    )

    title = models.CharField(max_length=20, verbose_name='名称')
    salary = models.FloatField(max_length=11, verbose_name='薪资')
    browse = models.IntegerField(default=0, null=True, verbose_name='浏览量')
    address = models.CharField(max_length=30, verbose_name='地址')
    experience = models.CharField(choices=EXPERIENCE_CHOICES, default=0, verbose_name='工作经验')
    education = models.CharField(choices=EDUCATION_CHOICES, default=8, verbose_name='学历')
    is_collect = models.BooleanField(default=False, verbose_name='收藏职位')
    person_count = models.IntegerField(max_length=4, verbose_name='招聘人数')
    duty_time = models.DateTimeField(verbose_name='到岗时间')
    age = models.IntegerField(max_length=2, verbose_name='年龄')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    merry = models.SmallIntegerField(choices=MERRY_CHOICES, default=0, verbose_name='婚况')
    language = models.CharField(verbose_name='语言')
    name = models.CharField(max_length=10, verbose_name='姓名')
    mobile = models.CharField(max_length=11, verbose_name='联系方式')
    desc = models.CharField(max_length=400, verbose_name='职位描述')

    # CASCADE: 级联，删除主表数据时同时一起删除外键表中数据, 级联删除。
    # pcompany = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE, verbose_name='企业')  # 外键

    class Meta:
        db_table = 'position'  # 指明数据库表名
        verbose_name = '职位'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.title