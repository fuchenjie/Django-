# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Active',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(verbose_name='省份', max_length=2, null=True, choices=[('M', '河南'), ('F', '北京')])),
                ('Active_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Active_Name', models.CharField(verbose_name='活动名称', max_length=100)),
                ('Active_StartDate', models.DateField(verbose_name='开始时间')),
                ('Active_EndDate', models.DateField(verbose_name='结束时间')),
                ('Active_UserName', models.CharField(verbose_name='客户名', max_length=100)),
                ('Active_IsDelete', models.IntegerField(verbose_name='是否删除', default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActiveType',
            fields=[
                ('ActiveType_ID', models.AutoField(primary_key=True, serialize=False)),
                ('ActiveType_Name', models.CharField(verbose_name='类型名', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
