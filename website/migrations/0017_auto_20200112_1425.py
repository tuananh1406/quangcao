# Generated by Django 2.2.4 on 2020-01-12 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20200108_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sanphamcon',
            old_name='baiviet_sanpham',
            new_name='sanpham_sanphamcha',
        ),
    ]