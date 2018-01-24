from django.db import models
#abstract抽象类     一般我们用它来归纳一些公共属性字段，然后继承它的子类可以继承这些字段
class Provice(models.Model):
    name=models.CharField(max_length=100)
    GENDER_CHOICE=((u'M',u'河南'),(u'F',u'北京'))
    gender=models.CharField('省份',max_length=2,choices=GENDER_CHOICE,null=True)
    class Meta:
        abstract=True
#活动类型
class ActiveType(models.Model):
    ActiveType_ID=models.AutoField(primary_key=True)
    ActiveType_Name=models.CharField(u'类型名',max_length=50)
    def __str__(self):
        return self.ActiveType_Name
#活动设置
class Active(Provice):
    Active_ID=models.AutoField(primary_key=True)
    Active_Name=models.CharField(u'活动名称',max_length=100)
    Active_StartDate=models.DateField(u'开始时间')
    Active_EndDate=models.DateField(u'结束时间')
    Active_UserName=models.CharField(u'客户名',max_length=100)
    Active_IsDelete=models.IntegerField(u'是否删除',default=0)
    def __str__(self):
        return self.Active_Name #设置列表中显示内容
    class Mate:#Meta选项
        verbose_name = '披萨”' #给你的模型类起一个更可读的名字如果不指定Django会自动在模型名称后加一个’s’
        verbose_name_plural='故事'
        ordering=['-Active_ID'] #排序设置'-order_date'表示降序'?order_date' # 随机排序，？表示随机
class test(models.Model):
    name=models.CharField(max_length=50)
    class Mate:
        managed=False #于Django会自动根据模型类生成映射的数据库表，如果你不希望Django这么做，可以把managed的值设置为False
