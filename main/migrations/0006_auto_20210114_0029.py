# Generated by Django 3.1.5 on 2021-01-13 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_client_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=30, verbose_name='Отчество')),
                ('position', models.CharField(max_length=10, verbose_name='Должность')),
                ('phone', models.DecimalField(decimal_places=0, max_digits=11, verbose_name='Телефон')),
                ('password', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Пароль')),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='password',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Пароль'),
        ),
    ]
