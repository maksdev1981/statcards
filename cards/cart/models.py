from django.db import models


# Справочники
class SPR_d1o_f10(models.Model):
    code = models.CharField(max_length=2, verbose_name='Код', unique=True)
    name = models.CharField(max_length=50, null=False, verbose_name='Наименование', unique=True)
    class Meta:
        verbose_name = 'Ф1.0Р1 Орган'
        verbose_name_plural = 'Ф1.0Р1 Органы'
    def __str__(self):
        return str(self.code) + ' - ' + self.name

class SPR_d01_f10(models.Model):
    code = models.CharField(max_length=2, verbose_name='Код', unique=True)
    name = models.CharField(max_length=100, null=False, verbose_name='Наименование')
    class Meta:
        verbose_name = 'Ф1.0Р1 Код территориального органа'
        verbose_name_plural = 'Ф1.0Р1 Коды территориальных органов'
    def __str__(self):
        return str(self.code) + ' - ' + self.name

class SPR_d02_f10(models.Model):
    code = models.CharField(max_length=1, verbose_name='Код', unique=True)
    name = models.CharField(max_length=50, null=False, verbose_name='Наименование')
    class Meta:
        verbose_name = 'Ф1.0Р2 Учесть'
        verbose_name_plural = 'Ф1.0Р2 Учести'
    def __str__(self):
        return str(self.code) + ' - ' + self.name

class SPR_d3o_f10(models.Model):
    code = models.CharField(max_length=1, verbose_name='Код', unique=True)
    name = models.CharField(max_length=50, null=False, verbose_name='Наименование')
    class Meta:
        verbose_name = 'Ф1.0Р3 Вид'
        verbose_name_plural = 'Ф1.0Р3 Виды'
    def __str__(self):
        return str(self.code) + ' - ' + self.name

class SPR_gas_org(models.Model):
    code = models.CharField(max_length=8, verbose_name='Код ГАСОРГ', unique=True)
    name = models.CharField(max_length=100, null=False, verbose_name='Наименование ГАСОРГ')
    class Meta:
        verbose_name = 'Ф1.0Р3 ГАС Орган'
        verbose_name_plural = 'Ф1.0Р3 ГАС Органы'
    def __str__(self):
        return str(self.code) + ' - ' + self.name

class SPR_d07k_f10(models.Model):
    code = models.CharField(max_length=1, verbose_name='Код', unique=True)
    name = models.CharField(max_length=100, null=False, verbose_name='Наименование')
    class Meta:
        verbose_name = 'Ф1.0Р7.1 Восстановлено на учет в числе ППЛ'
        verbose_name_plural = 'Ф1.0Р7.1 Восстановлены на учет в числе ППЛ'
    def __str__(self):
        return str(self.code) + ' - ' + self.name

class SPR_d08_f10(models.Model):
    code = models.CharField(max_length=2, verbose_name='Код', unique=True)
    name = models.CharField(max_length=100, null=False, verbose_name='Наименование')
    class Meta:
        verbose_name = 'Ф1.0Р8 Преступление предотвращено'
        verbose_name_plural = 'Ф1.0Р8 Преступления предотвращены'
    def __str__(self):
        return str(self.code) + ' - ' + self.name

class SPR_d09_f10(models.Model):
    code = models.CharField(max_length=5, verbose_name='Код', unique=True)
    name = models.CharField(max_length=100, null=False, verbose_name='Наименование')
    class Meta:
        verbose_name = 'Ф1.0Р9 Преступление выявлено'
        verbose_name_plural = 'Ф1.0Р9 Преступления выявлены'
    def __str__(self):
        return str(self.code) + ' - ' + self.name

class SPR_d09_1_f10(models.Model):
    code = models.CharField(max_length=1, verbose_name='Код', unique=True)
    name = models.CharField(max_length=100, null=False, verbose_name='Наименование')
    class Meta:
        verbose_name = 'Ф1.0Р9.1 Преступление выявлено по ...'
        verbose_name_plural = 'Ф1.0Р9.1 Преступления выявлены по ...'
    def __str__(self):
        return str(self.code) + ' - ' + self.name

class SPR_d10_f10(models.Model):
    code = models.CharField(max_length=4, verbose_name='Код', unique=True)
    name = models.CharField(max_length=100, null=False, verbose_name='Наименование')
    class Meta:
        verbose_name = 'Ф1.0Р10 Преступление возбуждено'
        verbose_name_plural = 'Ф1.0Р10 Преступления возбуждены'
    def __str__(self):
        return str(self.code) + ' - ' + self.name

class SPR_d10_1_f10(models.Model):
    code = models.CharField(max_length=4, verbose_name='Код', unique=True)
    name = models.CharField(max_length=100, null=False, verbose_name='Наименование')
    class Meta:
        verbose_name = 'Ф1.0Р10.1 Преступление возбуждено'
        verbose_name_plural = 'Ф1.0Р10.1 Преступления возбуждены'
    def __str__(self):
        return str(self.code) + ' - ' + self.name

class SPR_d10_2_f10(models.Model):
    code = models.CharField(max_length=3, verbose_name='Код', unique=True)
    name = models.CharField(max_length=100, null=False, verbose_name='Наименование')
    class Meta:
        verbose_name = 'Ф1.0Р10.2 Преступление возбуждено'
        verbose_name_plural = 'Ф1.0Р10.2 Преступления возбуждены'
    def __str__(self):
        return str(self.code) + ' - ' + self.name

class SPR_d10_3_f10(models.Model):
    code = models.CharField(max_length=5, verbose_name='Код', unique=True)
    name = models.CharField(max_length=100, null=False, verbose_name='Наименование')
    class Meta:
        verbose_name = 'Ф1.0Р10.3 Преступление возбуждено'
        verbose_name_plural = 'Ф1.0Р10.3 Преступления возбуждены'
    def __str__(self):
        return str(self.code) + ' - ' + self.name