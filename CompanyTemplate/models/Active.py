from django.db import models
#活动类型
class ActiveType(models.Model):
    ActiveType_ID=models.BigAutoField(primary_key=True)
    ActiveType_Name=models.CharField('类型名',max_length=50)
    def __str__(self):
        return self.ActiveType_Name
    class Mate:
        verbose_name = u"测试"
        verbose_name_plural = u"测试"
        app_label='CompanyTemplate'
#活动设置
class Active(models.Model):
    Active_ID=models.BigAutoField(primary_key=True)
    Active_Name=models.CharField('活动名称',max_length=100)
    Active_StartDate=models.DateField('开始时间')
    Active_EndDate=models.DateField('结束时间')
    Active_UserName=models.CharField('客户名',max_length=100)
    Active_IsDelete=models.IntegerField('是否删除',default=0)
    class Mate:
        verbose_name  =  '披萨'
        verbose_name_plural  =  '故事'
        app_label='CompanyTemplate'
