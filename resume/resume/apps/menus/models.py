from django.db import models

# Create your models here.
class Menu(models.Model):
    categoryname = models.CharField(verbose_name='分类名')
    order = models.IntegerField(verbose_name='顺序')
    first_page = models.CharField(verbose_name='首页')
    find_job = models.CharField(verbose_name='找工作')
    find_talent = models.CharField(verbose_name='找人才')
    mine = models.CharField(verbose_name='我的')


    class Meta:
        db_table = 'menus'
        verbose_name = '菜单表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.categoryname

