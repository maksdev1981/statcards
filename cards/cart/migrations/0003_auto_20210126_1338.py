# Generated by Django 3.1.5 on 2021-01-26 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20210126_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spr_d01_f10',
            name='code',
            field=models.CharField(max_length=2, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='spr_d01_f10',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='spr_d02_f10',
            name='code',
            field=models.CharField(max_length=1, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='spr_d1o_f10',
            name='code',
            field=models.CharField(max_length=2, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='spr_d3o_f10',
            name='code',
            field=models.CharField(max_length=1, verbose_name='Код'),
        ),
    ]