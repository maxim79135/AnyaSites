# Generated by Django 3.1.5 on 2021-03-23 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210323_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parameter',
            name='client',
        ),
    ]
