from django.db import models

# Create your models here.
class ActiveType(models.Model):
    ActiveType_ID=models.BigAutoField(primary_key=True)
    ActiveType_Name=models.CharField(max_length=50)
class Active(models.Model):
    Active_ID=models.BigAutoField(primary_key=True)
    Active_Name=models.CharField(max_length=100)
    Active_StartDate=models.DateField()
    Active_EndDate=models.DateField()

#模板1
class Mode1(models.Model):
    
