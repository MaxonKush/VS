# Generated by Django 3.1.2 on 2020-10-31 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg_log', '0002_auto_20201031_1723'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('id',)},
        ),
    ]