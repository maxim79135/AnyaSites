# Generated by Django 3.1.5 on 2021-02-14 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210214_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='password',
        ),
    ]
