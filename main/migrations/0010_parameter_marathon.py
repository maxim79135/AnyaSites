# Generated by Django 3.1.5 on 2021-02-14 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_client_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='marathon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.marathon', verbose_name='Марафон'),
        ),
    ]
