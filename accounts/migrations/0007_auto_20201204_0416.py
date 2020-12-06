# Generated by Django 3.1.2 on 2020-12-04 01:16

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20201105_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, help_text='Формат: <em>Якуба Коласа 5, кв. 8</em>.', max_length=50, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='driver_license',
            field=models.CharField(help_text='*', max_length=8, unique=True, verbose_name='№ лиценции'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='experience',
            field=models.IntegerField(help_text='*', validators=[accounts.models.validate_date], verbose_name='Опыт вождения'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='patronymic',
            field=models.CharField(help_text='*', max_length=50, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(help_text='*', max_length=13, unique=True, verbose_name='Телефон'),
        ),
    ]