# Generated by Django 3.1.2 on 2020-12-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201204_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='driver_license',
            field=models.CharField(help_text='*', max_length=8, unique=True, verbose_name='№ лицензии'),
        ),
    ]
