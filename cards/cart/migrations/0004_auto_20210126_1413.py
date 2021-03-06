# Generated by Django 3.1.5 on 2021-01-26 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20210126_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spr_d01_f10',
            name='code',
            field=models.CharField(max_length=2, unique=True, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='spr_d02_f10',
            name='code',
            field=models.CharField(max_length=1, unique=True, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='spr_d1o_f10',
            name='code',
            field=models.CharField(max_length=2, unique=True, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='spr_d3o_f10',
            name='code',
            field=models.CharField(max_length=1, unique=True, verbose_name='Код'),
        ),
    ]
