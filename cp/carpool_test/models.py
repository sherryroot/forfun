from django.db import models


# Create your models here.


class Orders_td(models.Model):
    Name = models.CharField(max_length=30, null=False)
    Tel = models.CharField(max_length=11, null=False)
    Addr = models.CharField(max_length=30, null=False)
    Time = models.CharField(max_length=10, null=False)
    Post = models.CharField(max_length=30, null=False)
    Num = models.CharField(max_length=5, null=False)
    To_where = models.CharField(max_length=5, null=False)

    # 修改表名字
    class Meta():
        db_table = '今天'


class Orders_tm(models.Model):
    Name = models.CharField(max_length=30, null=False)
    Tel = models.CharField(max_length=11, null=False)
    Addr = models.CharField(max_length=30, null=False)
    Time = models.CharField(max_length=10, null=False)
    Post = models.CharField(max_length=30, null=False)
    Num = models.CharField(max_length=5, null=False)
    To_where = models.CharField(max_length=30, null=False)

    # 修改表名字
    class Meta():
        db_table = '明天'


class Orders_af(models.Model):
    Name = models.CharField(max_length=30, null=False)
    Tel = models.CharField(max_length=11, null=False)
    Addr = models.CharField(max_length=30, null=False)
    Time = models.CharField(max_length=10, null=False)
    Post = models.CharField(max_length=30, null=False)
    Num = models.CharField(max_length=5, null=False)
    To_where = models.CharField(max_length=30, null=False)

    # 修改表名字
    class Meta():
        db_table = '后天'


