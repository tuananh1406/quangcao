# Generated by Django 2.2.4 on 2019-08-10 16:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20190810_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baiviet',
            name='baiviet_ngaydang',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Ngày đăng bài'),
        ),
    ]
